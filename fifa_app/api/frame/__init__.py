from flask_restplus import Namespace

from fifa_app.extensions import mongo
from .models import create_frame_model
from .dao import FrameDAO


# NAMESPACE
ns = Namespace('api/frame', 
                description = 'Frames related operations', 
                endpoint='frame')

db    = mongo.db.frames           # db collection
model = create_frame_model(ns)    # model
DAO   = FrameDAO(db, ns)         # record controller


from .routes import *
