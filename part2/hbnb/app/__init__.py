from flask import Flask
from flask_restx import Api

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    
    # Configs can go here
    app.config['RESTX_MASK_SWAGGER'] = False
    app.config['JSON_SORT_KEYS'] = False

    # Initialize API
    api = Api(app, version="1.0", title="HBnB API", description="HBnB Project API")

    # Import routes / resources
    from .services.user_service import ns as user_ns
    from .services.place_service import ns as place_ns
    from .services.amenity_service import ns as amenity_ns
    from .services.review_service import ns as review_ns

    # Add namespaces
    api.add_namespace(user_ns, path='/users')
    api.add_namespace(place_ns, path='/places')
    api.add_namespace(amenity_ns, path='/amenities')
    api.add_namespace(review_ns, path='/reviews')

    return app
