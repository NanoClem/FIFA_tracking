from flask_restplus import Namespace

from fifa_app.extensions import mongo
from .models import create_record_model
from .dao import RecordDAO


# NAMESPACE
ns = Namespace('api/frame', 
                description = 'Frames related operations', 
                endpoint='frame')

db    = mongo.db.frames           # db collection
model = create_record_model(ns)   # model
DAO   = RecordDAO(db, ns)         # record controller


from .routes import *
