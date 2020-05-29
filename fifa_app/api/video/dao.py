from flask import jsonify
from datetime import datetime
from bson.json_util import dumps
from bson.errors import InvalidId



class VideoDAO(object):
    """
    """

    def __init__(self, database, namespace):
        """
        """
        self.db = database
        self.ns = namespace


    def exists(self, data):
        """ Check if a document already exists in collection

        Parameter
        -----
        data (dict, json): document to check

        Returns
        -----
        True if exists, else False
        """
        return self.db.count_documents(data, limit = 1) != 0


    #---------------------------------------------
    #   GET
    #---------------------------------------------

    def getAll(self):
        """ Get all videos stored in database 
        """
        cursor = list(self.db.find({}))
        return jsonify(cursor)


    def get_video(self, data):
        """ Get one or many video matching with the payload
        """
        cursor = list(self.db.find(data))
        return jsonify(cursor)


    def getByID(self, id):
        """ Get a video by its id
        """
        try:
            data = self.db.find_one({"_id": id})
            return jsonify(data)
        except InvalidId:
            self.ns.abort(422, message="Invalid id {}".format(id), data={})
        

    #---------------------------------------------
    #   POST
    #---------------------------------------------

    def create_video(self, data):
        """ Create a new data document 
        """
        if self.exists(data):
            self.ns.abort(409, message="document already exists", data={})

        cpy_data = data
        cpy_data['created_at'] = datetime.now()
        res = self.db.insert_one(cpy_data)
        return jsonify( {'inserted_id': res.inserted_id} )


    def createMany(self, dataList):
        """ Create multiple videos
        """
        cpy_data = dataList
        for data in dataList:
            if self.exists(data):   # avoid duplicates
                cpy_data.remove(data)
            else:
                data['created_at'] = datetime.now()
        
        res = self.db.insert_many(cpy_data)
        return jsonify( {'inserted_ids': res.inserted_ids} )


    def update_video(self, id, data):
        """ Update a video
        """
        try:
            self.db.update_one({'_id': id}, {'$set': data})
            return ''
        except InvalidId:
            self.ns.abort(422, message="Invalid id {}".format(id), data={})


    #---------------------------------------------
    #   DELETE
    #---------------------------------------------

    def delete_video(self, video):
        """ Delete one or many video(s), matching with payload
        """
        self.db.delete(video)
        return ''


    def delete_by_id(self, id):
        """ Delete a data collection
        """
        try:
            self.db.delete_one({'_id': id})
            return ''
        except InvalidId:
            self.ns.abort(422, message="Invalid id {}".format(id), data={})