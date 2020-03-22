from flask import make_response
from flask_restplus import Namespace, Resource, fields
from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId

from fifa_app.extensions import mongo
from fifa_app.auth import token_required
from .models import create_team_model
from .DAO import TeamDAO


# namespace and its metadata
ns = Namespace('api/2', 
                description = 'Team related operations', 
                endpoint='team')

# mongo collection
db   = mongo.db.teams           # db collection
team = create_team_model(ns)    # team model
DAO  = TeamDAO(db, ns)          # team controller


from .routes import team_routes

