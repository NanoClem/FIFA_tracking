from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId

from flask import make_response
from flask_restplus import Resource

from ..frame import ns, db, DAO, model



#---------------------------------------------
#   MANY DOCUMENTS
#---------------------------------------------

@ns.route('/many', strict_slashes = False)     # strict_slashes setted to False so the debuger ignores it
@ns.response(404, 'Frame not found')
class FrameList(Resource):
    """ Get a list of all stored frames and allows to POST many frames
    """

    @ns.doc('get_all_frames') #, security='apikey')
    @ns.response(200, 'Success')
    #@ns.marshal_list_with(model)
    #@token_required
    def get(self):
        """ Return a list of all stored frames
        """
        return make_response(DAO.getAll(), 200)


    @ns.doc('create_many_frames')
    @ns.response(201, 'Frame successfuly created')
    @ns.expect([model])
    def post(self):
        """ Create many frames
        """
        return make_response(DAO.createMany(ns.payload), 201)


#---------------------------------------------
#   ONE OR MANY DOCUMENT
#---------------------------------------------

@ns.route('/', strict_slashes = False)
@ns.response(404, 'Frame not found')
class Frame(Resource):
    """
    """

    @ns.doc('create_one_frame')
    @ns.response(201, 'Frame successfuly created')
    @ns.expect(model)
    def post(self):
        """ Create a new frame
        """
        return make_response(DAO.create_frame(ns.payload), 201)


    @ns.doc('get_one_frame')
    @ns.response(200, 'Success')
    @ns.expect(model)
    def get(self):
        """ Get one or many frames matching with given body
        """
        return make_response(DAO.get_frame(ns.payload), 200)

    
    @ns.doc('delete_frame')
    @ns.response(204, 'Frame successfuly deleted')
    @ns.expect(model)
    def delete(self):
        """ Delete one or many frame(s) matching with given body
        """
        return make_response(DAO.delete_frame(ns.payload), 204)


#---------------------------------------------
#   CRUD BY FRAME NUMBER
#---------------------------------------------

@ns.route("/<int:num>")
@ns.response(404, 'Frame not found')
@ns.param('num', 'The frame number')
class FrameByNum(Resource):
    """ Get, update or delete one frame by its num
    """

    @ns.doc('update_frame')
    @ns.response(204, 'Frame successfuly updated')
    @ns.expect(model)
    def put(self, num):
        """ Update a frame by its num
        """
        return make_response(DAO.update_frame(num, ns.payload), 204)


#---------------------------------------------
#   CRUD BY ID
#---------------------------------------------

@ns.route("/<objectid:id>")
@ns.response(404, 'Frame not found')
@ns.param('id', 'The frame unique identifier')
class FrameByID(Resource):
    """ Get, update or delete one frame
    """

    @ns.doc('get_frame_by_id')
    @ns.response(200, 'Success')
    def get(self, id):
        """ Returns a frame by its id
        """
        return make_response(DAO.getByID(id), 200)

    @ns.doc('delete_frame_by_id')
    @ns.response(204, 'Frame successfuly deleted')
    def delete(self, id):
        """ Delete a frame by its id
        """
        return make_response(DAO.delete_by_id(id), 204)

    @ns.doc('update_frame')
    @ns.response(204, 'Frame successfuly updated')
    @ns.expect(model)
    def put(self, id):
        """ Update a frame by its id
        """
        return make_response(DAO.update_frame(id, ns.payload), 204)


#---------------------------------------------
#   GET FRAMES BY VIDEO ID
#---------------------------------------------

@ns.route("/video/<string:id>")
@ns.response(404, 'Frame not found')
@ns.response(200, 'Success')
@ns.param('id', 'The video unique identifier')
class FrameByVideoID(Resource):
    """ Get one or many frames by their video id
    """

    @ns.doc('get_frame_by_video_id')
    def get(self, id):
        """ Returns one or many frames by their video id
        """
        return make_response(DAO.getByVideoID(id), 200)