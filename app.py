from flask import Flask, jsonify
from flask_restful import Api
from recovery.controller import ForgotPasswordResource, ResetPasswordResource

from users.controller import UserListResource, UserResource
from auth.controller import LoginResource
from users.models import db
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
jwt = JWTManager(app)
api = Api(app)
app.config.from_pyfile('config.py')
db.init_app(app)
mail = Mail(app)


@api.representation('application/json')
def output_json(data, code, headers=None):
    """Custom JSON response formatting."""
    resp = jsonify(data)
    resp.status_code = code
    resp.headers.extend(headers or {})
    return resp


api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(LoginResource, '/login')
api.add_resource(ForgotPasswordResource, '/forgot_password')
api.add_resource(ResetPasswordResource, '/reset_password')

if __name__ == '__main__':
    app.run(debug=True)
