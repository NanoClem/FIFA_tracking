from flask import Flask
from flask_pymongo import PyMongo

from configs import settings as stg



def create_app():
    """ Instanciate a Flask app and add configs"""
    app = Flask(__name__)
    app.config['MONGO_URI'] = stg.MONGO_URI
    app.config['MONGO_DBNAME'] = stg.MONGO_DBNAME
    return app


def create_mongo(app, uri):
    """ Instanciate MongoDB database"""
    return PyMongo(app, uri)
