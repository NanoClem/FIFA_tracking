from flask_restplus import Namespace

from fifa_app.extensions import mongo
from .models import create_team_model
from .dao import TeamDAO


# NAMESPACE
ns = Namespace('api/team', 
                description = 'Team related operations', 
                endpoint='team')

db    = mongo.db.teams           # db collection
model = create_team_model(ns)    # model
DAO   = TeamDAO(db, ns)          # controller


from .routes import *

