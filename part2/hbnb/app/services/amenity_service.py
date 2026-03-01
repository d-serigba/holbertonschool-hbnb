# app/services/amenity_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource

ns = Namespace('amenities', description='Amenity operations')


@ns.route('/')
class AmenityList(Resource):
    def get(self):
        """Retourne toutes les amenities"""
        amenities = current_app.facade.get_amenities()
        return amenities, 200  # déjà des dicts

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
