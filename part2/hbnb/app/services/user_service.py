# app/services/user_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource

ns = Namespace('users', description='User operations')


@ns.route('/')
class UserList(Resource):
    def get(self):
        """Retourne tous les users"""
        users = current_app.facade.get_users()
        return users, 200  # users est déjà une liste de dicts

    def post(self):
        """Crée un nouvel user"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400
        try:
            new_user = current_app.facade.create_user(data)
            return new_user, 201  # new_user est déjà un dict
        except Exception as e:
            return {"error": str(e)}, 400


@ns.route('/<string:user_id>')
class User(Resource):
    def get(self, user_id):
        """Retourne un user par ID"""
        users = current_app.facade.get_users()
        user = next((u for u in users if u["id"] == user_id), None)
        if not user:
            return {"error": "User not found"}, 404
        return user, 200
