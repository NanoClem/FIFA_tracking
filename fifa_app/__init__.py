from flask import Flask

from .extensions import mongo
from fifa_app.api import register_api
from fifa_app.views import register_views
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
    app = Flask(__name__, template_folder='views/templates')

    # APP CONFIGS
    app.config.from_object(config_object)
    app.url_map.converters['objectid'] = ObjectIdConverter
    app.json_encoder = MongoJSONEncoder

    # LOAD EXTENSIONS
    mongo.init_app(app)

    # REGISTER APP ELEMENTS
    register_api(app)
    register_views(app)
    
    return app