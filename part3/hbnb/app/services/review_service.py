# app/services/review_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity

ns = Namespace('reviews', description='Operations related to reviews')

# ---------------- Modèles Swagger ----------------
review_create_model = ns.model('ReviewCreate', {
    'text': fields.String(required=True, description='Texte de la review', example='Super endroit!'),
    'rating': fields.Integer(required=True, min=1, max=5, description='Note de 1 à 5', example=5),
    'place_id': fields.String(required=True, description='ID de la place', example='uuid-de-la-place')
})

review_update_model = ns.model('ReviewUpdate', {
    'text': fields.String(description='Texte de la review', example='Vraiment top!'),
    'rating': fields.Integer(description='Note de 1 à 5', example=4)
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

        # Vérification des champs obligatoires
        required_fields = ['text', 'place_id', 'rating']
        for field in required_fields:
            if field not in data:
                return {"error": f"{field} is required"}, 400

        # Vérification de la validité de la note
        if not (1 <= int(data['rating']) <= 5):
            return {"error": "Rating must be between 1 and 5"}, 400

        user_id = get_jwt_identity()
        data['user_id'] = user_id

        # Vérifier si la place existe
        place = current_app.facade.get_place(data['place_id'])
        if not place:
            return {"error": "Place not found"}, 404

        # Empêcher de noter sa propre place
        if place.owner_id == user_id:
            return {"error": "Cannot review your own place"}, 403

        # Empêcher les doublons de review par le même utilisateur sur la même place
        existing_review = current_app.facade.get_review_by_user_and_place(user_id, data['place_id'])
        if existing_review:
            return {"error": "You have already reviewed this place"}, 400

        # Création via la Facade
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

        # Seul l'auteur ou un admin peut modifier
        if not current_user.is_admin and review.user_id != user_id:
            return {"error": "Forbidden: not the author"}, 403

        data = request.get_json()
        updated_review = current_app.facade.update_review(review_id, data)
        return updated_review.to_dict(), 200

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
