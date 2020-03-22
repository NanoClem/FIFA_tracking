from flask_restplus import Namespace

from fifa_app.extensions import mongo
from .models import create_team_model
from .dao import TeamDAO


# NAMESPACE
ns = Namespace('api/2', 
                description = 'Team related operations', 
                endpoint='team')

db   = mongo.db.teams           # db collection
team = create_team_model(ns)    # team model
DAO  = TeamDAO(db, ns)          # team controller


from .routes import *

