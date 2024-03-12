from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from functools import wraps
from flask import abort, request


def check_permission(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        if current_user_id != kwargs["user_id"]:
            abort(403, "Você não tem permissão para acessar este recurso")
        return func(*args, **kwargs)

    return decorated_function


def jwt_required_optional(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization", None)
        if not token:
            abort(401, "Token JWT não fornecido")
        try:
            verify_jwt_in_request()
        except Exception:
            abort(401, "Token JWT inválido")
        return func(*args, **kwargs)

    return decorated_function
