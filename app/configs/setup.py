from flask import Flask
from flask_pymongo import PyMongo

from configs import settings as stg
from utils import MongoJSONEncoder, ObjectIdConverter



def create_app():
    """ Instanciate a Flask app and add configs"""
    app = Flask(__name__)
    app.config['MONGO_URI'] = stg.MONGO_URI
    app.config['MONGO_DBNAME'] = stg.MONGO_DBNAME
    app.json_encoder = MongoJSONEncoder
    app.url_map.converters['objectid'] = ObjectIdConverter
    return app


def create_mongo(app, uri):
    """ Instanciate MongoDB database"""
    return PyMongo(app, uri)
