from flask_restplus import Api

# from fifa_app.modules.auth import authorizations


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
    from ..video import ns as ns_video
    from ..frame import ns as ns_frame
    from ..team import ns as ns_team
    
    api.add_namespace(ns_video)  # adding video namespace
    api.add_namespace(ns_frame)  # adding frame namespace
    api.add_namespace(ns_team)   # adding team namespace
    api.init_app(app)
