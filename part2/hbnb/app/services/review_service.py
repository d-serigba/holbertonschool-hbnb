# app/services/review_service.py
from flask import request, current_app
from flask_restx import Namespace, Resource

ns = Namespace('reviews', description='Review operations')


@ns.route('/')
class ReviewList(Resource):
    def get(self):
        """Retourne toutes les reviews"""
        reviews = current_app.facade.get_reviews()
        return reviews, 200  # déjà des dicts

    def post(self):
        """Crée une nouvelle review"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400
        try:
            new_review = current_app.facade.create_review(data)
            return new_review, 201
        except ValueError as ve:
            return {"error": str(ve)}, 400
        except Exception as e:
            return {"error": str(e)}, 400


@ns.route('/<string:review_id>')
class Review(Resource):
    def get(self, review_id):
        """Retourne une review par ID"""
        review = current_app.facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return review.to_dict(), 200

    def put(self, review_id):
        """Met à jour une review existante"""
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400
        try:
            updated_review = current_app.facade.update_review(review_id, data)
            if not updated_review:
                return {"error": "Review not found"}, 404
            return updated_review.to_dict(), 200
        except ValueError as ve:
            return {"error": str(ve)}, 400
        except Exception as e:
            return {"error": str(e)}, 400

    def delete(self, review_id):
        """Supprime une review existante"""
        success = current_app.facade.delete_review(review_id)
        if not success:
            return {"error": "Review not found"}, 404
        return {"message": "Review deleted"}, 200
