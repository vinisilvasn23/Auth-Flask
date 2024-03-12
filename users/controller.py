from flask_restful import Resource, reqparse
from permissions.jwt import check_permission, jwt_required_optional
from users.database import get_session
from .service import find_by_id, update, desactive, create_user
from .models import User

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="name is required")
parser.add_argument("email", type=str, required=True, help="Email is required")
parser.add_argument("password", type=str, required=True, help="Senha is required")
parser.add_argument("active", type=bool, required=False, default=True, help="Ativo")

parser_update_user = reqparse.RequestParser()
parser_update_user.add_argument("name", type=str, help="Name is required")
parser_update_user.add_argument("email", type=str, help="Email is required")
parser_update_user.add_argument("active", type=bool, help="Ativo")


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users]

    def post(self):
        data = parser.parse_args()
        name = data["name"]
        email = data["email"]
        password = data["password"]
        user = create_user(name, email, password)
        if user:
            return user.to_dict(), 201
        else:
            return {"message": "User already exists"}, 400


class UserResource(Resource):
    @jwt_required_optional
    @check_permission
    def get(self, user_id):
        session = get_session()
        user = find_by_id(user_id, session)
        if user is None:
            return {"error": "User not found"}, 404
        return user.to_dict()

    @jwt_required_optional
    @check_permission
    def patch(self, user_id):
        data = parser_update_user.parse_args()

        user_return = update(user_id, data)

        return user_return, 200

    @jwt_required_optional
    @check_permission
    def delete(self, user_id):
        return desactive(user_id, False)
