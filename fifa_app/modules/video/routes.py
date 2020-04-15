from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId

from flask import make_response
from flask_restplus import Resource

from fifa_app.modules.video import ns, db, model, DAO



#---------------------------------------------
#   MANY DOCUMENTS
#---------------------------------------------

@ns.route('/many', strict_slashes = False)     # strict_slashes setted to False so the debuger ignores it
@ns.response(404, 'Video not found')
class VideoList(Resource):
    """ Get a list of all stored videos and allows to POST many videos
    """

    @ns.doc('get_all_videos') #, security='apikey')
    @ns.response(200, 'Success')
    #@ns.marshal_list_with(model)
    #@token_required
    def get(self):
        """ Return a list of all stored videos
        """
        return make_response(DAO.getAll(), 200)


    @ns.doc('create_many_videos')
    @ns.response(201, 'Video successfuly created')
    @ns.expect([model])
    def post(self):
        """ Create many videos
        """
        return make_response(DAO.createMany(ns.payload), 201)


#---------------------------------------------
#   POST ONE DOCUMENT
#---------------------------------------------

@ns.route('/', strict_slashes = False)
@ns.response(404, 'Video not found')
class Video(Resource):
    """
    """

    @ns.doc('create_one_video')
    @ns.response(201, 'Video successfuly created')
    @ns.expect(model)
    def post(self):
        """ Create a new video
        """
        return make_response(DAO.create_video(ns.payload), 201)


    @ns.doc('get_one_video')
    @ns.response(200, 'Success')
    @ns.expect(model)
    def get(self):
        """ Get one or many videos matching with given body
        """
        return make_response(DAO.get_video(ns.payload), 200)

    
    @ns.doc('delete_video')
    @ns.response(204, 'Video successfuly deleted')
    @ns.expect(model)
    def delete(self):
        """ Delete one or many video(s) mathcing with given body
        """
        return make_response(DAO.delete_video(ns.payload), 204)
        

#---------------------------------------------
#   CRUD BY ID
#---------------------------------------------

@ns.route("/<objectid:id>")
@ns.response(404, 'Video not found')
@ns.param('id', 'The video unique identifier')
class FrameByID(Resource):
    """ Get, update or delete one video
    """

    @ns.doc('get_video_by_id')
    @ns.response(200, 'Success')
    @ns.marshal_with(model)
    def get(self, id):
        """ Returns a video by its id
        """
        return make_response(DAO.getByID(id), 200)


    @ns.doc('update_video')
    @ns.response(204, 'Video successfuly updated')
    @ns.expect(model)
    def put(self, id):
        """ Update a video by its id
        """
        return make_response(DAO.update_video(id, ns.payload), 204)


    @ns.doc('delete_video_by_id')
    @ns.response(204, 'Video successfuly deleted')
    def delete(self, id):
        """ Delete a video by its id
        """
        return make_response(DAO.delete_by_id(id), 204)