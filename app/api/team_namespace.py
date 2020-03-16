from flask import make_response
from flask_restplus import Namespace, Resource, fields
from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId

from configs import mongo
from .models import create_team_model
from .DAO import TeamDAO
from .auth import token_required


# namespace and its metadata
ns = Namespace('api', description = 'Team related operations', endpoint='team')
db = mongo.db.records


#=============================================================
#   MODEL
#=============================================================
record = create_team_model(ns)


#=============================================================
#   DAO
#=============================================================
DAO = TeamDAO(db, ns)


#=============================================================
#   ROUTING
#=============================================================
single_route = "/team"
many_route   = "/teams"

#---------------------------------------------
#   MANY DATA
#---------------------------------------------
@ns.route(many_route, strict_slashes = False)     # strict_slashes setted to False so the debuger ignores it
class TeamList(Resource):
    """
    Get a list of all stored data and allows POST for multiple documents
    """

    @ns.doc('get all teams') #, security='apikey')
    #@ns.marshal_list_with(record) #envelope='data')
    #@token_required
    def get(self):
        """Return a list of all team data"""
        return make_response(DAO.getAll(), 200)


    @ns.doc('create many teams')
    @ns.expect(record)
    def post(self):
        """Create multiple documents"""
        return make_response(DAO.createMany(ns.payload), 201)


#---------------------------------------------
#   POST ONE DATA
#---------------------------------------------
@ns.route(single_route, strict_slashes = False)
class Team(Resource):
    """
    """

    @ns.doc('create one team')
    @ns.expect(record)
    def post(self):
        """Create a new team"""
        return make_response(DAO.create(ns.payload), 201)


#---------------------------------------------
#   CRUD BY ID
#---------------------------------------------
@ns.route(single_route + "/<objectid:id>")
@ns.response(404, 'Team data not found')
@ns.param('id', 'The team unique identifier')
class TeamByID(Resource):
    """
    Show a single document, update one, or delete one
    """

    @ns.doc('Get a team by its id')
    @ns.marshal_with(record)
    def get(self, id):
        """Returns a single team by its id"""
        return make_response(DAO.getByID(id), 200)


    @ns.doc('update a team')
    def put(self, id):
        """Update a team"""
        DAO.update(id, ns.payload)
        return make_response('', 201)


    @ns.doc('delete a team')
    @ns.response(204, 'Team deleted')
    def delete(self, id):
        """Delete a team"""
        DAO.delete(id)
        return make_response('', 204)