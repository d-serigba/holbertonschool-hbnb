# app/auth/decorators.py
from flask import current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps


def admin_required(fn):
    """Decorator: vérifie que l'utilisateur connecté est admin"""
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = current_app.facade.get_user(user_id)
        if not user or not getattr(user, "is_admin", False):
            return {"error": "Admin privileges required"}, 403
        return fn(*args, **kwargs)
    return wrapper

