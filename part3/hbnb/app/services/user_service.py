# app/services/user_service.py

from flask import request, current_app
from flask_restx import Namespace, Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from functools import wraps

ns = Namespace('users', description='User operations')


# ---------------- Decorator admin ----------------
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = current_app.facade.get_user(user_id)
        if not user or not getattr(user, "is_admin", False):
            return {"error": "Admin privileges required"}, 403
        return fn(*args, **kwargs)
    return wrapper


# ---------------- USERS LIST ----------------
@ns.route('/')
class UserList(Resource):

    @jwt_required()
    def get(self):
        """Retourne tous les users (authentifié)"""
        users = current_app.facade.get_users()
        return users, 200

    @admin_required
    def post(self):
        """Crée un nouvel user (admin seulement)"""
        data = request.get_json()
        if not data:
            return {"error": "Invalid input"}, 400

        required = ["first_name", "last_name", "email", "password"]
        for field in required:
            if field not in data:
                return {"error": f"{field} is required"}, 400

        user = current_app.facade.create_user(data)
        return user, 201


# ---------------- LOGIN ----------------
@ns.route('/login/')
class Login(Resource):

    def post(self):
        """Login et retourne un JWT"""
        data = request.get_json()
        if not data or "email" not in data or "password" not in data:
            return {"error": "Email and password required"}, 400

        user = current_app.facade.get_user_by_email(data["email"])
        if not user or not user.check_password(data["password"]):
            return {"error": "Invalid credentials"}, 401

        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, 200


# ---------------- USER BY ID ----------------
@ns.route('/<string:user_id>/')
class UserResource(Resource):

    @jwt_required()
    def get(self, user_id):
        """Retourne un user par ID"""
        user = current_app.facade.get_user(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return user, 200

    @admin_required
    def put(self, user_id):
        """Met à jour un user (admin seulement)"""
        data = request.get_json()
        user = current_app.facade.update_user(user_id, data)
        if not user:
            return {"error": "User not found"}, 404
        return user, 200

    @admin_required
    def delete(self, user_id):
        """Supprime un user (admin seulement)"""
        success = current_app.facade.delete_user(user_id)
        if not success:
            return {"error": "User not found"}, 404
        return {"message": "User deleted"}, 200
