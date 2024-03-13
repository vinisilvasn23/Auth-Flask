from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from flask_bcrypt import check_password_hash
from users.models import User


parser = reqparse.RequestParser()
parser.add_argument("email", type=str, required=True, help="Email is required")
parser.add_argument("password", type=str, required=True, help="password is required")


class LoginResource(Resource):
    def post(self):
        data = parser.parse_args()

        user = User.query.filter_by(email=data['email']).first()

        if not user or not user.active or not check_password_hash(user.password, data['password']):
            return {'erro': 'Email or password incorrect.!'}, 401

        token = create_access_token(identity=user.id)
        return {"token": token}
