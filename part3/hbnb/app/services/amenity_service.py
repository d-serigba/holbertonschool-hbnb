# app/services/amenity_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource

ns = Namespace('amenities', description='Amenity operations')


@ns.route('/')
class AmenityList(Resource):

    def get(self):
        """Retourne toutes les amenities"""
        amenities = current_app.facade.get_amenities()
        return amenities, 200

    def post(self):
        """Crée une nouvelle amenity"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        try:
            new_amenity = current_app.facade.create_amenity(data)
            return new_amenity, 201
        except Exception as e:
            return {"error": str(e)}, 400


@ns.route('/<string:amenity_id>')
class AmenityResource(Resource):

    def get(self, amenity_id):
        """Retourne une amenity par ID"""
        amenity = current_app.facade.get_amenities()
        item = next((a for a in amenity if a["id"] == amenity_id), None)
        if not item:
            return {"error": "Amenity not found"}, 404
        return item, 200

    def put(self, amenity_id):
        """Met à jour une amenity"""
        data = request.get_json()
        updated = current_app.facade.update_amenity(amenity_id, data)
        if not updated:
            return {"error": "Amenity not found"}, 404
        return updated, 200

    def delete(self, amenity_id):
        """Supprime une amenity"""
        success = current_app.facade.delete_amenity(amenity_id)
        if not success:
            return {"error": "Amenity not found"}, 404
        return {"message": "Amenity deleted"}, 200
