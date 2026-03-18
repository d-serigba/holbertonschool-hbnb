# app/services/amenity_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps

ns = Namespace('amenities', description='Amenity operations')

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


@ns.route('/')
class AmenityList(Resource):

    def get(self):
        """Retourne toutes les amenities"""
        amenities = current_app.facade.get_amenities()
        return [a.to_dict() for a in amenities], 200

    @admin_required
    def post(self):
        """Crée une nouvelle amenity (admin seulement)"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        new_amenity = current_app.facade.create_amenity(data)
        return new_amenity.to_dict(), 201


@ns.route('/<string:amenity_id>')
class AmenityResource(Resource):

    def get(self, amenity_id):
        """Retourne une amenity par ID"""
        amenities = current_app.facade.get_amenities()
        item = next((a.to_dict() for a in amenities if a.id == amenity_id), None)
        if not item:
            return {"error": "Amenity not found"}, 404
        return item, 200

    @admin_required
    def put(self, amenity_id):
        """Met à jour une amenity (admin seulement)"""
        data = request.get_json()
        updated = current_app.facade.update_amenity(amenity_id, data)
        if not updated:
            return {"error": "Amenity not found"}, 404
        return updated.to_dict(), 200

    @admin_required
    def delete(self, amenity_id):
        """Supprime une amenity (admin seulement)"""
        success = current_app.facade.delete_amenity(amenity_id)
        if not success:
            return {"error": "Amenity not found"}, 404
        return {"message": "Amenity deleted"}, 200
