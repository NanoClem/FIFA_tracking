from flask import jsonify
from datetime import datetime
from bson.json_util import dumps
from bson.errors import InvalidId



class TeamDAO(object):
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
    #   BY ID
    #---------------------------------------------

    def getByID(self, id):
        """Return data from one record

        Parameter
        ----
        id (int) : the document unique id
        
        """
        try:
            data = self.db.find_one({"_id": id})
            if data != None:
                return jsonify( {'message': 'success', 'data': data} )
            self.ns.abort(404, message="Id {} doesn't exist".format(id), data={})
        except InvalidId:
            self.ns.abort(422, message="Invalid id {}".format(id), data={})
        

    def update(self, id, data):
        """Update a data collection"""
        crypto = self.getByID(id)
        self.db.update_one(crypto, data)


    def delete(self, id):
        """Delete a data collection"""
        data = self.getByID(id)
        self.db.delete_one(data)



    #---------------------------------------------
    #   BY TEAMS ID
    #---------------------------------------------

    def getByTeamId(self, id):
        """Return all data collections related to a team
        
        Parameter
        -----
        id (string) : the team id
        """
        cursor = list(self.db.find({"team_id": id}))
        if cursor :
            return jsonify( {'message': 'success', 'data': cursor} )
        self.ns.abort(404, message="record {} doesn't exist".format(id), data={})



    #---------------------------------------------
    #   COMMON OPERATIONS
    #---------------------------------------------

    def getAll(self):
        """ Get all documents in database """
        cursor = list(self.db.find({}))
        return jsonify( {'message': 'success', 'data': cursor} )



    def create(self, data):
        """ Create a new data document """
        # if self.exists(data):
        #     self.ns.abort(409, message="document already exists", data={})
        # else:
        cpy_data = data
        cpy_data['created_at'] = datetime.now()
        ins = self.db.insert_one(cpy_data)
        return jsonify( {'message': 'success', 'data': {'inserted_id': ins.inserted_id}} )



    def createMany(self, dataList):
        """ Create multiple data documents"""
        cpy_data = dataList
        # PRE-PROCESS DATA IN LIST
        for data in dataList:
            if self.exists(data):   # avoid duplicates
                cpy_data.remove(data)
            else:
                data['created_at'] = datetime.now()
        
        ins = self.db.insert_many(cpy_data)
        return jsonify( {'message': 'success', 'data': {'inserted_ids': ins.inserted_ids}} )