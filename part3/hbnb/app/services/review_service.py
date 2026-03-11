# review_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource

ns = Namespace('reviews', description='Operations related to reviews')

@ns.route('/')
class ReviewList(Resource):
    """Liste toutes les reviews ou crée une nouvelle review"""

    def get(self):
        """Retourne toutes les reviews"""
        reviews = current_app.facade.get_reviews()
        return [r.to_dict() for r in reviews], 200

    def post(self):
        """Crée une nouvelle review"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        required_fields = ['text', 'place_id', 'user_id']
        for field in required_fields:
            if field not in data:
                return {"error": f"{field} is required"}, 400

        review = current_app.facade.create_review(data)
        return review.to_dict(), 201


@ns.route('/<string:review_id>')
class ReviewResource(Resource):
    """Gère une review spécifique par ID"""

    def get(self, review_id):
        """Récupère une review par son ID"""
        review = current_app.facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return review.to_dict(), 200

    def put(self, review_id):
        """Met à jour une review existante"""
        review = current_app.facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        # Mise à jour seulement du texte pour simplifier
        if 'text' in data:
            review.text = data['text']
            current_app.facade.update_review(review_id, {'text': data['text']})

        return review.to_dict(), 200

    def delete(self, review_id):
        """Supprime une review existante"""
        review = current_app.facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        current_app.facade.delete_review(review_id)
        return {"message": "Review deleted"}, 200
