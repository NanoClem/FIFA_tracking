
def register_views(app):
    """ Register all MethodViews to app
    """
    from .views import Index

    # ADD VIEWS URL
    app.add_url_rule('/index', view_func=Index.as_view('index'), methods=['GET'])