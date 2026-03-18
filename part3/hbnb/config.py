# config.py

import os
from datetime import timedelta

class Config:
    """Configuration générale pour l'application HBnB"""

    # ---------------- Flask / SQLAlchemy ----------------
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///hbnb.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ---------------- JWT ----------------
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "une_clef_super_secrète")  # à remplacer en prod
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # Durée de vie du token

    # ---------------- Flask-RestX ----------------
    RESTX_MASK_SWAGGER = False
    JSON_SORT_KEYS = False
