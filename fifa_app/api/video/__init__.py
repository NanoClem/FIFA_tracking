from flask_restplus import Namespace

from fifa_app.extensions import mongo
from .models import create_video_model
from .dao import VideoDAO


# NAMESPACE
ns = Namespace('api/video', 
                description = 'Video related operations', 
                endpoint='video')

db    = mongo.db.videos          # db collection
model = create_video_model(ns)   # model
DAO   = VideoDAO(db, ns)         # controller


from .routes import *

