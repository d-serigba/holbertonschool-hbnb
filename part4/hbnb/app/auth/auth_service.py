# app/auth/auth_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token

ns = Namespace('auth', description='Authentication operations')

# ---------------- Modèle Swagger ----------------
login_model = ns.model('Login', {
    'email': fields.String(required=True, description='Adresse email', example='admin@hbnb.com'),
    'password': fields.String(required=True, description='Mot de passe', example='admin1234')
})


# ---------------- LOGIN ----------------
@ns.route('/login/')
class Login(Resource):
    @ns.expect(login_model)
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
