from flask import Flask, jsonify, render_template, request
from flask_restful import Api
from recovery.controller import ForgotPasswordResource, ResetPasswordResource

from recovery.service import reset_password, verify_password_reset_token
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

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password_page():
    token = request.args.get('token')
    if request.method == 'POST':
        token_form = request.form.get('token')
        password = request.form['password']
        print(token)
        user_id = verify_password_reset_token(token_form)
        if user_id:
            reset_password(user_id, password)
            return "Password reset successful."
        else:
            return "Invalid Token."
    else:
        return render_template('reset_password.html', token=token)
api.add_resource(ResetPasswordResource, '/reset_password_api')

if __name__ == '__main__':
    app.run(debug=True)
