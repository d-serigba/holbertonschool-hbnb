# app/auth/auth_api.py
from flask import request
from flask_restx import Namespace, Resource
from .auth_service import AuthService

ns = Namespace("auth", description="Authentication operations")
auth_service = AuthService()

@ns.route("/login/")
class Login(Resource):
    def post(self):
        """Login et retourne un JWT"""
        data = request.get_json()
        if not data or "email" not in data or "password" not in data:
            return {"error": "Email and password required"}, 400

        token = auth_service.login(data["email"], data["password"])
        if not token:
            return {"error": "Invalid credentials"}, 401

        return {"access_token": token}, 200
