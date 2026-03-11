# app/persistence/repository.py

from app.models.base_model import db


class SQLAlchemyRepository:
    """Repository générique pour gérer les opérations CRUD"""

    def add(self, obj):
        """Ajoute un objet à la base"""
        db.session.add(obj)
        db.session.commit()
        return obj

    def get_all(self, model_class):
        """Retourne tous les objets d'un modèle"""
        return model_class.query.all()

    def get(self, model_class, obj_id):
        """Retourne un objet par son id"""
        return model_class.query.get(obj_id)

    def update(self, obj):
        """Met à jour un objet existant"""
        db.session.commit()
        return obj

    def delete(self, obj):
        """Supprime un objet"""
        db.session.delete(obj)
        db.session.commit()
