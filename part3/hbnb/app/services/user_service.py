# app/services/user_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from app.auth.decorators import admin_required
 
ns = Namespace('users', description='User operations')
 
# ---------------- Modèles Swagger ----------------
user_create_model = ns.model('UserCreate', {
    'first_name': fields.String(required=True, description='Prénom', example='John'),
    'last_name': fields.String(required=True, description='Nom', example='Doe'),
    'email': fields.String(required=True, description='Email', example='john@hbnb.com'),
    'password': fields.String(required=True, description='Mot de passe', example='john1234'),
    'is_admin': fields.Boolean(description='Admin ?', example=False)
})
 
user_update_model = ns.model('UserUpdate', {
    'first_name': fields.String(description='Prénom', example='John'),
    'last_name': fields.String(description='Nom', example='Doe'),
    'email': fields.String(description='Email', example='john@hbnb.com'),
    'password': fields.String(description='Mot de passe', example='john1234'),
    'is_admin': fields.Boolean(description='Admin ?', example=False)
})
 
 
# ---------------- USERS LIST ----------------
@ns.route('/')
class UserList(Resource):
    @jwt_required()
    def get(self):
        """Retourne tous les users (authentifié)"""
        users = current_app.facade.get_users()
        return users, 200
 
    @admin_required
    @ns.expect(user_create_model)
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
    @ns.expect(user_update_model)
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
