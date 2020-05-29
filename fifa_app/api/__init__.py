from flask_restplus import Api


# API constructor
api = Api(
    title = "RESTful-fifa",
    description = "interact with data from FIFA",
    version = 1.0
)


def register_api(app):
    """ Registering namespaces and the api to the app
    """
    from .video import ns as ns_video
    from .frame import ns as ns_frame
    from .team import ns as ns_team
    
    # ADD NAMESPACES
    api.add_namespace(ns_video)
    api.add_namespace(ns_frame)
    api.add_namespace(ns_team)

    # REGISTER API TO APP
    api.init_app(app)
