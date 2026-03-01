# app/models/base_model.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True  # Ne crée pas de table directement

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        """Ajoute ou met à jour l'objet dans la base"""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Supprime l'objet de la base"""
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour JSON"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
