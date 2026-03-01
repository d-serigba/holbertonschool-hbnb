from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# --- MODÈLES POUR LA DOCUMENTATION ET LA VALIDATION ---
# Utilisé pour représenter l'owner dans la réponse du logement
user_model = api.model('PlaceOwner', {
    'id': fields.String(description='Owner ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Utilisé pour représenter les équipements dans la réponse
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

# Modèle principal pour la création et la mise à jour
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude coordinate'),
    'longitude': fields.Float(required=True, description='Longitude coordinate'),
    'owner_id': fields.String(required=True, description='ID of the owner')
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    def post(self):
        """Register a new place"""
        place_data = api.payload
        
        # Validation des données (Le "Vigile")
        if place_data.get('price', 0) < 0:
            return {'error': 'Price must be a positive value'}, 400
        if not (-90 <= place_data.get('latitude', 0) <= 90):
            return {'error': 'Latitude must be between -90 and 90'}, 400
        if not (-180 <= place_data.get('longitude', 0) <= 180):
            return {'error': 'Longitude must be between -180 and 180'}, 400
            
        try:
            new_place = facade.create_place(place_data)
            if not new_place:
                return {'error': 'Owner not found or invalid'}, 400
            
            return {
                'id': new_place.id,
                'title': new_place.title,
                'description': new_place.description,
                'price': new_place.price,
                'latitude': new_place.latitude,
                'longitude': new_place.longitude,
                'owner_id': new_place.owner.id
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [{
            'id': p.id, 
            'title': p.title, 
            'latitude': p.latitude, 
            'longitude': p.longitude
        } for p in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    def get(self, place_id):
        """Récupérer les détails d'un logement avec son propriétaire et ses avis"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        
        # On récupère les avis pour ce lieu via la façade
        reviews = facade.get_reviews_by_place(place_id)
        
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': [{
                'id': a.id,
                'name': a.name
            } for a in place.amenities],
            'reviews': [{ # <--- C'EST CETTE PARTIE QUI MANQUAIT
                'id': r.id,
                'text': r.text,
                'rating': r.rating,
                'user_name': f"{r.user.first_name} {r.user.last_name}"
            } for r in reviews]
        }, 200

    @api.expect(place_model)
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        
        if 'price' in place_data and place_data['price'] < 0:
            return {'error': 'Price must be a positive value'}, 400
            
        updated_place = facade.update_place(place_id, place_data)
        if not updated_place:
            return {'error': 'Place not found'}, 404
            
        return {'message': 'Place updated successfully'}, 200

@api.route('/<place_id>/amenities/<amenity_id>')
class PlaceAmenityResource(Resource):
    def post(self, place_id, amenity_id):
        """Link an amenity to a place"""
        updated_place = facade.add_amenity_to_place(place_id, amenity_id)
        if not updated_place:
            return {'error': 'Place or Amenity not found'}, 404
        return {'message': 'Amenity added successfully to the place'}, 200

@api.route('/<place_id>/reviews')
class PlaceReviewList(Resource):
    def get(self, place_id):
        """Récupérer tous les avis d'un logement spécifique"""
        reviews = facade.get_reviews_by_place(place_id)
        return [{'id': r.id, 'text': r.text, 'rating': r.rating} for r in reviews], 200
