from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId

from flask import make_response
from flask_restplus import Resource

from fifa_app.api.record_namespace import ns, db, DAO, record

single_route = "/record"
many_route   = "/records"


#---------------------------------------------
#   MANY DOCUMENTS
#---------------------------------------------
@ns.route(many_route, strict_slashes = False)     # strict_slashes setted to False so the debuger ignores it
class RecordList(Resource):
    """
    Get a list of all stored data and allows POST for multiple documents
    """

    @ns.doc('get all collections') #, security='apikey')
    #@ns.marshal_list_with(record) #envelope='data')
    #@token_required
    def get(self):
        """Return a list of all records data"""
        return make_response(DAO.getAll(), 200)


    @ns.doc('create many collections')
    @ns.expect(record)
    def post(self):
        """Create multiple data records"""
        return make_response(DAO.createMany(ns.payload), 201)


#---------------------------------------------
#   POST ONE DOCUMENT
#---------------------------------------------
@ns.route(single_route, strict_slashes = False)
class Record(Resource):
    """
    """

    @ns.doc('create one collection')
    @ns.expect(record)
    def post(self):
        """Create a new record data"""
        return make_response(DAO.create(ns.payload), 201)


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
        return make_response(DAO.getByID(id), 200)


    @ns.doc('update_record')
    def put(self, id):
        """Update a data collection"""
        DAO.update(id, ns.payload)
        return make_response('', 201)


    @ns.doc('delete_record')
    @ns.response(204, 'Record deleted')
    def delete(self, id):
        """Delete a data collection"""
        DAO.delete(id)
        return make_response('', 204)


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
        return make_response(DAO.getByTeamId(name), 200)