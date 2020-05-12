
def register_views(app):
    """ Register all MethodViews to app
    """
    from .views import Index, Heatmap

    # ADD VIEWS URL
    app.add_url_rule('/index', view_func=Index.as_view('index'), methods=['GET'])
    app.add_url_rule('/heatmap', view_func=Heatmap.as_view('heatmap'), methods=['GET'])