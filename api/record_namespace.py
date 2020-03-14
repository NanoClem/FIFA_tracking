from flask_restplus import Namespace, Resource, fields
from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId

from configs import mongo
from .models import create_record_model
from .DAO import recordDAO
from .auth import token_required


# namespace and its metadata
ns = Namespace('api', description = 'Records related operations', endpoint='record')
db = mongo.db.records


#=============================================================
#   MODEL
#=============================================================
record = create_record_model(ns)


#=============================================================
#   DAO
#=============================================================
DAO = recordDAO(db, ns)


#=============================================================
#   ROUTING
#=============================================================
single_route = "/record"
many_route   = "/records"

#---------------------------------------------
#   MANY DATA
#---------------------------------------------
@ns.route(many_route, strict_slashes = False)     # strict_slashes setted to False so the debuger ignores it
class RecordList(Resource):
    """
    Get a list of all stored data and allows POST for multiple documents
    """

    @ns.doc('get all collections') #, security='apikey')
    @ns.marshal_list_with(record) #envelope='data')
    #@token_required
    def get(self):
        """Return a list of all records data"""
        return DAO.getAll(), 200


    @ns.doc('create many collections')
    @ns.expect(record)
    @ns.marshal_list_with(record, code=201)
    def post(self):
        """Create multiple data records"""
        return DAO.createMany(ns.payload), 201


#---------------------------------------------
#   POST ONE DATA
#---------------------------------------------
@ns.route(single_route, strict_slashes = False)
class Record(Resource):
    """
    """

    @ns.doc('create one collection')
    @ns.expect(record)
    def post(self):
        """Create a new record data"""
        return DAO.create(ns.payload), 201


#---------------------------------------------
#   CRUD BY ID
#---------------------------------------------
@ns.route(single_route + "/<objectid:id>")
@ns.response(404, 'Record data not found')
@ns.param('id', 'The record data unique identifier')
class RecordByID(Resource):
    """
    Show a single data item, update one, or delete one
    """

    @ns.doc('get_record_by_id')
    @ns.marshal_with(record)
    def get(self, id):
        """Returns a single data collection by id"""
        return DAO.getByID(id), 200


    @ns.doc('update_record')
    def put(self, id):
        """Update a data collection"""
        DAO.update(id, ns.payload)
        return '', 201


    @ns.doc('delete_record')
    @ns.response(204, 'Record deleted')
    def delete(self, id):
        """Delete a data collection"""
        DAO.delete(id)
        return '', 204


#---------------------------------------------
#   CRUD BY TEAM
#---------------------------------------------
@ns.route(many_route + "/teams/<objectid:id>")
@ns.response(404, 'Record data not found')
@ns.param('id', 'A reference to the team by its id ')
class RecordsTeamById(Resource):
    """
    Show records related to a team
    """

    @ns.doc('get_teams_record_by_id')
    @ns.marshal_list_with(record, envelope='data')
    def get(self, name):
        """Returns all data collections related to a team"""
        return DAO.getByTeamId(name), 200