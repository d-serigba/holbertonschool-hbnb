# app/services/place_service.py

from flask import request, current_app
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps

ns = Namespace('places', description='Place operations')


@ns.route('/')
class PlaceList(Resource):

    def get(self):
        """Retourne toutes les places (public)"""
        places = current_app.facade.get_places()
        return [p.to_dict() for p in places], 200

    @jwt_required()
    def post(self):
        """Crée une nouvelle place (authentifié)"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400
        if 'title' not in data:
            return {"error": "title is required"}, 400
        if 'price' not in data:
            return {"error": "price is required"}, 400

        user_id = get_jwt_identity()
        data['owner_id'] = user_id

        new_place = current_app.facade.create_place(data)
        return new_place.to_dict(), 201


@ns.route('/<string:place_id>')
class PlaceResource(Resource):

    def get(self, place_id):
        """Retourne une place par ID (public)"""
        place = current_app.facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return place.to_dict(), 200

    @jwt_required()
    def put(self, place_id):
        """Met à jour une place existante"""
        place = current_app.facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        user_id = get_jwt_identity()
        current_user = current_app.facade.get_user(user_id)
        if not current_user.is_admin and place.owner_id != user_id:
            return {"error": "Forbidden: not the owner"}, 403

        data = request.get_json()
        updated_place = current_app.facade.update_place(place_id, data)
        return updated_place.to_dict(), 200

    @jwt_required()
    def delete(self, place_id):
        """Supprime une place existante"""
        place = current_app.facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        user_id = get_jwt_identity()
        current_user = current_app.facade.get_user(user_id)
        if not current_user.is_admin and place.owner_id != user_id:
            return {"error": "Forbidden: not the owner"}, 403

        success = current_app.facade.delete_place(place_id)
        if not success:
            return {"error": "Place could not be deleted"}, 400
        return {"message": "Place deleted"}, 200
