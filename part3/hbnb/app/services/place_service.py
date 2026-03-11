# app/services/place_service.py

from flask import request, current_app
from flask_restx import Namespace, Resource

ns = Namespace('places', description='Place operations')


@ns.route('/')
class PlaceList(Resource):

    def get(self):
        """Retourne toutes les places"""
        places = current_app.facade.get_places()
        # S'assure que chaque place est un dict
        return [p.to_dict() if not isinstance(p, dict) else p for p in places], 200

    def post(self):
        """Crée une nouvelle place"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        try:
            new_place = current_app.facade.create_place(data)
            return new_place.to_dict() if not isinstance(new_place, dict) else new_place, 201
        except Exception as e:
            return {"error": str(e)}, 400


@ns.route('/<string:place_id>')
class PlaceResource(Resource):

    def get(self, place_id):
        """Retourne une place par ID"""
        place = current_app.facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return place.to_dict() if not isinstance(place, dict) else place, 200

    def put(self, place_id):
        """Met à jour une place existante"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        updated_place = current_app.facade.update_place(place_id, data)
        if not updated_place:
            return {"error": "Place not found"}, 404

        return updated_place.to_dict() if not isinstance(updated_place, dict) else updated_place, 200

    def delete(self, place_id):
        """Supprime une place"""
        success = current_app.facade.delete_place(place_id)
        if not success:
            return {"error": "Place not found"}, 404

        return {"message": "Place deleted"}, 200
