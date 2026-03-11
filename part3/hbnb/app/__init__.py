from flask import Flask
from flask_restx import Api
from .models.base_model import db
from .facade import HBnBFacade


def create_app(config_object=None):
    app = Flask(__name__)

    # ---------------- Config ----------------
    if config_object:
        app.config.from_object(config_object)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hbnb.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.config['RESTX_MASK_SWAGGER'] = False
    app.config['JSON_SORT_KEYS'] = False

    # ---------------- Facade ----------------
    app.facade = HBnBFacade()

    # ---------------- API ----------------
    api = Api(app, version="1.0", title="HBnB API", description="HBnB Project API")

    # ---------------- Patch JSON pour objets SQLAlchemy ----------------
    def object_to_dict(obj):
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        if isinstance(obj, list):
            return [object_to_dict(o) for o in obj]
        return obj

    @api.representation('application/json')
    def output_json(data, code, headers=None):
        from json import dumps
        dumped = dumps(object_to_dict(data), indent=4) + "\n"
        resp = app.response_class(dumped, mimetype='application/json', status=code)
        if headers:
            resp.headers.extend(headers)
        return resp

    # ---------------- Namespaces ----------------
    from .services.user_service import ns as user_ns
    from .services.place_service import ns as place_ns
    from .services.amenity_service import ns as amenity_ns
    from .services.review_service import ns as review_ns

    api.add_namespace(user_ns, path='/users')
    api.add_namespace(place_ns, path='/places')
    api.add_namespace(amenity_ns, path='/amenities')
    api.add_namespace(review_ns, path='/reviews')

    # ---------------- Création DB ----------------
    with app.app_context():
        db.create_all()

    return app
