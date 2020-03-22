from flask_restplus import Api

from .auth import authorizations


# API constructor
api = Api(
    title = "RESTful-fifa",
    description = "interact with data from FIFA",
    version = 1.0
    #authorizations = authorizations
)


def register_api(app):
    """ Registering namespaces and the api to the app
    """
    from .record_namespace import ns as ns_record
    from .team_namespace import ns as ns_team
    
    api.add_namespace(ns_record)  # adding record namespace
    api.add_namespace(ns_team)    # adding team namespace
    api.init_app(app)
