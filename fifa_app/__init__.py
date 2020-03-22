from flask import Flask

from fifa_app.api import register_api
from .extensions import mongo
from .utils import MongoJSONEncoder, ObjectIdConverter



# CREATE FLASK APP
def create_app(config_object='fifa_app.settings'):
    """ Instanciate a Flask app

    Parameters
    -----
    config_object : file dedicated to configuration in Flask env

    Returns
    -----
    A Flask app object
    """
    # FLASK APP OBJECT
    app = Flask(__name__)

    # APP CONFIGS
    app.config.from_object(config_object)
    app.url_map.converters['objectid'] = ObjectIdConverter
    app.json_encoder = MongoJSONEncoder

    # REGISTER ELEMENTS TO APP
    mongo.init_app(app)
    register_api(app)
    
    return app