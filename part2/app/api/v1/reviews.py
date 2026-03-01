from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    def post(self):
        """Create a new review"""
        review_data = api.payload
        new_review = facade.create_review(review_data)
        if not new_review:
            return {'error': 'User or Place not found'}, 400
        
        return {
            'id': new_review.id,
            'text': new_review.text,
            'rating': new_review.rating,
            'user_id': new_review.user.id,
            'place_id': new_review.place.id
        }, 201

    def get(self):
        """List all reviews"""
        reviews = facade.get_all_reviews()
        return [{'id': r.id, 'text': r.text, 'rating': r.rating} for r in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    def get(self, review_id):
        """Get review by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return {
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user': review.user.first_name,
            'place': review.place.title
        }, 200

    @api.expect(review_model)
    def put(self, review_id):
        """Update review"""
        updated_review = facade.update_review(review_id, api.payload)
        if not updated_review:
            return {'error': 'Review not found'}, 404
        return {'message': 'Review updated successfully'}, 200

    def delete(self, review_id):
        """Delete review"""
        if not facade.delete_review(review_id):
            return {'error': 'Review not found'}, 404
        return {'message': 'Review deleted successfully'}, 200

from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Texte de l avis'),
    'rating': fields.Integer(required=True, description='Note de 1 à 5'),
    'user_id': fields.String(required=True, description='ID de l auteur'),
    'place_id': fields.String(required=True, description='ID du logement')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    def post(self):
        """Créer un nouvel avis"""
        review_data = api.payload
        # Validation du rating
        if not (1 <= review_data.get('rating', 0) <= 5):
            return {'error': 'La note doit être entre 1 et 5'}, 400
            
        new_review = facade.create_review(review_data)
        if not new_review:
            return {'error': 'Utilisateur ou Lieu non trouvé'}, 404
            
        return {'id': new_review.id, 'message': 'Review created successfully'}, 201

    def get(self):
        """Lister tous les avis"""
        reviews = facade.get_all_reviews()
        return [{'id': r.id, 'text': r.text, 'rating': r.rating} for r in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    def get(self, review_id):
        """Détails d'un avis"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return {
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.user.id,
            'place_id': review.place.id
        }, 200

    def delete(self, review_id):
        """Supprimer un avis (Le pouvoir du CEO)"""
        if facade.delete_review(review_id):
            return {'message': 'Review deleted successfully'}, 200
        return {'error': 'Review not found'}, 404
