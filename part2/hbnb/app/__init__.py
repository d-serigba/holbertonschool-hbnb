# app/__init__.py
from flask import Flask
from flask_restx import Api
from .models.base_model import db
from .facade import HBnBFacade  # Façade corrigée pour tes modèles

def create_app():
    app = Flask(__name__)

    # Config SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hbnb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialise SQLAlchemy avec l'app
    db.init_app(app)

    # Config API RESTX
    app.config['RESTX_MASK_SWAGGER'] = False
    app.config['JSON_SORT_KEYS'] = False
    api = Api(app, version="1.0", title="HBnB API", description="HBnB Project API")

    # Initialise la façade
    app.facade = HBnBFacade()

    # Import des services
    from .services.user_service import ns as user_ns
    from .services.place_service import ns as place_ns
    from .services.amenity_service import ns as amenity_ns
    from .services.review_service import ns as review_ns

    # Ajout des namespaces à l'API
    api.add_namespace(user_ns, path='/users')
    api.add_namespace(place_ns, path='/places')
    api.add_namespace(amenity_ns, path='/amenities')
    api.add_namespace(review_ns, path='/reviews')

    # Crée la base de données si elle n'existe pas
    with app.app_context():
        db.create_all()

    return app
