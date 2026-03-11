# app/services/user_service.py

from flask import request, current_app
from flask_restx import Namespace, Resource

ns = Namespace('users', description='User operations')


@ns.route('/')
class UserList(Resource):

    def get(self):
        """Retourne tous les users"""
        users = current_app.facade.get_users()
        return users, 200

    def post(self):
        """Crée un nouvel user"""
        data = request.get_json()

        if not data:
            return {"error": "No input data provided"}, 400

        try:
            new_user = current_app.facade.create_user(data)
            return new_user, 201
        except Exception as e:
            return {"error": str(e)}, 400


@ns.route('/<string:user_id>')
class UserResource(Resource):

    def get(self, user_id):
        """Retourne un user par ID"""
        user = current_app.facade.get_user(user_id)

        if not user:
            return {"error": "User not found"}, 404

        return user, 200


    def put(self, user_id):
        """Met à jour un user"""
        data = request.get_json()

        if not data:
            return {"error": "No input data provided"}, 400

        user = current_app.facade.update_user(user_id, data)

        if not user:
            return {"error": "User not found"}, 404

        return user, 200


    def delete(self, user_id):
        """Supprime un user"""

        success = current_app.facade.delete_user(user_id)

        if not success:
            return {"error": "User not found"}, 404

        return {"message": "User deleted"}, 200
