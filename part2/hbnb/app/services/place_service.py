# app/services/place_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource

ns = Namespace('places', description='Place operations')


@ns.route('/')
class PlaceList(Resource):
    def get(self):
        """Retourne toutes les places"""
        places = current_app.facade.get_places()
        return places, 200  # déjà des dicts

    def post(self):
        """Crée une nouvelle place"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400
        try:
            new_place = current_app.facade.create_place(data)
            return new_place, 201  # déjà un dict
        except ValueError as ve:
            return {"error": str(ve)}, 400
        except Exception as e:
            return {"error": str(e)}, 400


@ns.route('/<string:place_id>')
class Place(Resource):
    def get(self, place_id):
        """Retourne une place par ID"""
        place = current_app.facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return place.to_dict(), 200  # ici on garde to_dict car get_place retourne un objet

    def put(self, place_id):
        """Met à jour une place existante"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400
        try:
            updated_place = current_app.facade.update_place(place_id, data)
            if not updated_place:
                return {"error": "Place not found"}, 404
            return updated_place, 200  # déjà un dict
        except ValueError as ve:
            return {"error": str(ve)}, 400
        except Exception as e:
            return {"error": str(e)}, 400
