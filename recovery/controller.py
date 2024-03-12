from flask_restful import Resource, reqparse
from .service import (
    verify_password_reset_token,
    reset_password,
    generate_password_reset_token,
    find_user_by_email,
    send_password_reset_email
)
import pysnooper

@pysnooper.snoop()
class ForgotPasswordResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, required=True, help="Email is required")
        args = parser.parse_args()

        email = args["email"]
        user = find_user_by_email(email)
        if user:
            token = generate_password_reset_token(user.id)
            send_password_reset_email(user.email, token)
            return {"message": "Password reset token sent successfully."}, 200
        else:
            return {"error": "User not found!"}, 404

@pysnooper.snoop()
class ResetPasswordResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, required=True, help="Token is required")
        parser.add_argument(
            "password", type=str, required=True, help="Password is required"
        )
        args = parser.parse_args()

        token = args["token"]
        password = args["password"]

        user_id = verify_password_reset_token(token)
        if user_id:
            reset_password(user_id, password)
            return {"message": "Password reset successful"}, 200
        else:
            return {"error": "invalid Token"}, 400
