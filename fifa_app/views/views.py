from flask import render_template
from flask.views import MethodView



class Index(MethodView):
    """ Base index view of the app
    """
    def get(self):
        return render_template('index.html', title='Welcome')