from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId

from flask import make_response
from flask_restplus import Resource

from fifa_app.modules.team import ns, db, model, DAO



#---------------------------------------------
#   MANY DOCUMENTS
#---------------------------------------------

@ns.route('/many', strict_slashes = False)     # strict_slashes setted to False so the debuger ignores it
@ns.response(404, 'Team not found')
class TeamList(Resource):
    """ Get a list of all stored teams and allows to POST many teams
    """

    @ns.doc('get_all_teams') #, security='apikey')
    @ns.response(200, 'Success')
    #@ns.marshal_list_with(model)
    #@token_required
    def get(self):
        """ Return a list of all stored teams
        """
        return make_response(DAO.getAll(), 200)


    @ns.doc('create_many_teams')
    @ns.response(201, 'Team successfuly created')
    @ns.expect([model])
    def post(self):
        """ Create many teams
        """
        return make_response(DAO.createMany(ns.payload), 201)


#---------------------------------------------
#   POST ONE DOCUMENT
#---------------------------------------------

@ns.route('/', strict_slashes = False)
@ns.response(404, 'Team not found')
class Team(Resource):
    """
    """

    @ns.doc('create_one_team')
    @ns.response(201, 'Team successfuly created')
    @ns.expect(model)
    def post(self):
        """ Create a new team
        """
        return make_response(DAO.create_team(ns.payload), 201)


    @ns.doc('get_one_team')
    @ns.response(200, 'Success')
    @ns.expect(model)
    def get(self):
        """ Get one or many teams matching with given body
        """
        return make_response(DAO.get_team(ns.payload), 200)

    
    @ns.doc('delete_team')
    @ns.response(204, 'Team successfuly deleted')
    @ns.expect(model)
    def delete(self):
        """ Delete one or many team(s) mathcing with given body
        """
        return make_response(DAO.delete_team(ns.payload), 204)


#---------------------------------------------
#   CRUD BY TEAM NAME
#---------------------------------------------

@ns.route("/<string:name>")
@ns.response(404, 'Team not found')
@ns.param('name', 'The team name')
class TeamByName(Resource):
    """ Get, update or delete one team by its num
    """

    @ns.doc('update_frame')
    @ns.response(204, 'Frame successfuly updated')
    @ns.expect(model)
    def put(self, num):
        """ Update a frame by its id
        """
        return make_response(DAO.update_frame(num, ns.payload), 204)


#---------------------------------------------
#   CRUD BY ID
#---------------------------------------------

@ns.route("/<objectid:id>")
@ns.response(404, 'Team not found')
@ns.param('id', 'The team unique identifier')
class FrameByID(Resource):
    """ Get, update or delete one team
    """

    @ns.doc('get_team_by_id')
    @ns.response(200, 'Success')
    @ns.marshal_with(model)
    def get(self, id):
        """ Returns a team by its id
        """
        return make_response(DAO.getByID(id), 200)


    @ns.doc('update_team')
    @ns.response(204, 'Team successfuly updated')
    @ns.expect(model)
    def put(self, id):
        """ Update a team by its id
        """
        return make_response(DAO.update_team(id, ns.payload), 204)


    @ns.doc('delete_team_by_id')
    @ns.response(204, 'Team successfuly deleted')
    def delete(self, id):
        """ Delete a team by its id
        """
        return make_response(DAO.delete_by_id(id), 204)