# app/services/amenity_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource, fields
from app.auth.decorators import admin_required
 
ns = Namespace('amenities', description='Amenity operations')
 
# ---------------- Modèles Swagger ----------------
amenity_create_model = ns.model('AmenityCreate', {
    'name': fields.String(required=True, description='Nom', example='Jacuzzi'),
    'description': fields.String(description='Description', example='Jacuzzi extérieur')
})
 
amenity_update_model = ns.model('AmenityUpdate', {
    'name': fields.String(description='Nom', example='WiFi 6'),
    'description': fields.String(description='Description', example='Connexion très rapide')
})
 
 
@ns.route('/')
class AmenityList(Resource):
    def get(self):
        """Retourne toutes les amenities"""
        amenities = current_app.facade.get_amenities()
        return [a.to_dict() for a in amenities], 200
 
    @admin_required
    @ns.expect(amenity_create_model)
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
    @ns.expect(amenity_update_model)
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
