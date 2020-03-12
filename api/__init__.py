from flask_restplus import Api

from .record_namespace import ns as ns_record
from .auth import authorizations


# API constructor
api = Api(
    title = "RESTful-fifa",
    description = "interact with records data from FIFA",
    version = 1.0
    #authorizations = authorizations
)


def register_api(app):
    """ Registering namespaces and the api to the app
    """
    api.add_namespace(ns_record)  # Add namespace
    api.init_app(app)
