from flask import jsonify
from datetime import datetime
from bson.json_util import dumps
from bson.errors import InvalidId



class FrameDAO(object):
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
        """ Get all frames stored in database 
        """
        cursor = list(self.db.find({}))
        return jsonify(cursor)


    def get_frame(self, data):
        """ Get one or many frame matching with the payload
        """
        cursor = list(self.db.find(data))
        return jsonify(cursor)


    def getByID(self, id):
        """ Get a frame by its id
        """
        try:
            data = self.db.find_one({"_id": id})
            return jsonify(data)
        except InvalidId:
            self.ns.abort(422, message="Invalid id {}".format(id), data={})
        

    #---------------------------------------------
    #   POST
    #---------------------------------------------

    def create_frame(self, data):
        """ Create a new data document
        """
        if self.exists(data):
            self.ns.abort(409, message="document already exists", data={})

        cpy_data = data
        cpy_data['created_at'] = datetime.now()
        res = self.db.insert_one(cpy_data)
        return jsonify( {'inserted_id': res.inserted_id} )


    def createMany(self, dataList):
        """ Create multiple data documents
        """
        cpy_data = dataList
        for data in dataList:
            if self.exists(data):   # avoid duplicates
                cpy_data.remove(data)
            else:
                data['created_at'] = datetime.now()
        
        res = self.db.insert_many(cpy_data)
        return jsonify( {'inserted_ids': res.inserted_ids} )


    def update_frame(self, num, data):
        """ Update a frame
        """
        frame = self.db.find({'num': num})
        update = {'$set': data}
        self.db.update_one(frame, update)
        return ''


    #---------------------------------------------
    #   DELETE
    #---------------------------------------------

    def delete_frame(self, frame):
        """ Delete one or many frame(s), matching with payload
        """
        self.db.delete(frame)
        return ''


    def delete_by_id(self, id):
        """ Delete a data collection
        """
        self.db.delete_one({'_id': id})
        return ''