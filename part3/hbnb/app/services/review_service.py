# app/services/review_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
 
ns = Namespace('reviews', description='Operations related to reviews')
 
# ---------------- Modèles Swagger ----------------
review_create_model = ns.model('ReviewCreate', {
    'text': fields.String(required=True, description='Texte de la review', example='Super endroit!'),
    'place_id': fields.String(required=True, description='ID de la place', example='aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa')
})
 
review_update_model = ns.model('ReviewUpdate', {
    'text': fields.String(description='Texte de la review', example='Vraiment top!')
})
 
 
@ns.route('/')
class ReviewList(Resource):
    def get(self):
        """Retourne toutes les reviews (public)"""
        reviews = current_app.facade.get_reviews()
        return [r.to_dict() for r in reviews], 200
 
    @jwt_required()
    @ns.expect(review_create_model)
    def post(self):
        """Crée une nouvelle review (authentifié)"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400
        required_fields = ['text', 'place_id']
        for field in required_fields:
            if field not in data:
                return {"error": f"{field} is required"}, 400
        user_id = get_jwt_identity()
        data['user_id'] = user_id
        place = current_app.facade.get_place(data['place_id'])
        if not place:
            return {"error": "Place not found"}, 404
        if place.owner_id == user_id:
            return {"error": "Cannot review your own place"}, 403
        existing_review = current_app.facade.get_review_by_user_and_place(user_id, data['place_id'])
        if existing_review:
            return {"error": "You have already reviewed this place"}, 400
        review = current_app.facade.create_review(data)
        return review.to_dict(), 201
 
 
@ns.route('/<string:review_id>')
class ReviewResource(Resource):
    def get(self, review_id):
        """Récupère une review par son ID (public)"""
        review = current_app.facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return review.to_dict(), 200
 
    @jwt_required()
    @ns.expect(review_update_model)
    def put(self, review_id):
        """Met à jour une review existante"""
        review = current_app.facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        user_id = get_jwt_identity()
        current_user = current_app.facade.get_user(user_id)
        if not current_user.is_admin and review.user_id != user_id:
            return {"error": "Forbidden: not the author"}, 403
        data = request.get_json()
        review = current_app.facade.update_review(review_id, data)
        return review.to_dict(), 200
 
    @jwt_required()
    def delete(self, review_id):
        """Supprime une review existante"""
        review = current_app.facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        user_id = get_jwt_identity()
        current_user = current_app.facade.get_user(user_id)
        if not current_user.is_admin and review.user_id != user_id:
            return {"error": "Forbidden: not the author"}, 403
        current_app.facade.delete_review(review_id)
        return {"message": "Review deleted"}, 200
