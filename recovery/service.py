from datetime import datetime, timedelta, timezone
from flask import current_app, render_template_string
from flask_jwt_extended import JWTManager, create_access_token, decode_token
from users.database import get_session
from users.models import User
from flask_mail import Mail, Message

mail = Mail()

jwt = JWTManager()


def find_user_by_email(email):
    session = get_session()
    user = session.query(User).filter_by(email=email).first()
    return user

def generate_password_reset_token(user_id):
    expires = datetime.now(timezone.utc) + timedelta(hours=1)
    token_payload = {"user_id": user_id, "exp": expires}
    token = create_access_token(identity=token_payload)
    return token


def verify_password_reset_token(token):
    try:
        token_payload = decode_token(token)
        expiration_time = datetime.fromtimestamp(token_payload.get("exp", 0), timezone.utc)
        if datetime.now(timezone.utc) <= expiration_time:
            return token_payload.get("sub", {}).get("user_id")
    except Exception as e:
        print(f"Error verifying password reset token: {e}")
    return None


def reset_password(user_id, new_password):
    session = get_session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.set_password(new_password)
        session.commit() 
        return True
    else:
        return False


def send_password_reset_email(email, token):
    mail = current_app.extensions.get('mail')
    if not mail:
        raise ValueError("Flask-Mail not initialized")

    sender = current_app.config.get('MAIL_USERNAME')
    if not sender:
        raise ValueError("MAIL_DEFAULT_SENDER not configured")

    reset_password_url = f"http://127.0.0.1:5000/reset_password?token={token}"
    
    msg = Message(subject="Password Reset",
                  sender="your-email@example.com",
                  recipients=[email])
    
    html = render_template_string("""
    <p>Hello,</p>
    <p>You've requested to reset your password. Please click on the following link to reset your password:</p>
    <p><a href="{{ reset_password_url }}">Reset Password</a></p>
    <p>If you did not request this, please ignore this email.</p>
    <p>Best regards,</p>
    <p>User Auth</p>
    """, reset_password_url=reset_password_url)
    
    msg.html = html

    mail.send(msg)
    
    return "Password reset email sent successfully"