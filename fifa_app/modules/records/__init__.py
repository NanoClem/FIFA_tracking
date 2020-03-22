from flask_restplus import Namespace

from fifa_app.extensions import mongo
from .models import create_record_model
from .dao import RecordDAO


# NAMESPACE
ns = Namespace('api/1', 
                description = 'Records related operations', 
                endpoint='record')

db     = mongo.db.records           # db collection
record = create_record_model(ns)    # model
DAO    = RecordDAO(db, ns)          # record controller


from .routes import *
