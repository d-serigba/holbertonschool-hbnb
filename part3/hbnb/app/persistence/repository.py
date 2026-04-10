# app/persistence/repository.py
from app.models.base_model import db
from app.models.review import Review

class SQLAlchemyRepository:
    def __init__(self):
        pass

    @property
    def session(self):
        return db.session

    def add(self, obj):
        self.session.add(obj)
        self.session.commit()
        return obj

    def update(self, obj):
        self.session.commit()
        return obj

    def delete(self, obj):
        self.session.delete(obj)
        self.session.commit()
        return True

    def get(self, model_class, obj_id):
        return self.session.get(model_class, obj_id)

    def get_all(self, model_class):
        return self.session.query(model_class).all()

    def get_by_email(self, model_class, email):
        return self.session.query(model_class).filter_by(email=email).first()

    def get_review_by_user_and_place(self, user_id, place_id):
        return self.session.query(Review).filter_by(user_id=user_id, place_id=place_id).first()
