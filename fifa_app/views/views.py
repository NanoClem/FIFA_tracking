from flask import render_template
from flask.views import MethodView
import json


class Index(MethodView):
    """ Base index view of the app
    """
    def get(self):
        return render_template('index.html', title='Welcome')


class Heatmap(MethodView):
    """ Heatmap chart page
    """
    def get(self):
        return render_template('heatmap.html', title='Heatmap')