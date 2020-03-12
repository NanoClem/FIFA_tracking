from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId



class recordDAO(object):
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
            data = self.db.find_one({"_id": ObjectId(id)})
            if data != None:
                return data
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
        cursor = list(self.db.find({"team_id": ObjectId(id)}))
        if cursor :
            return cursor
        self.ns.abort(404, message="record {} doesn't exist".format(id), data={})


    #---------------------------------------------
    #   COMMON OPERATIONS
    #---------------------------------------------

    def getAll(self):
        """ Get all documents in database """
        cursor = self.db.find({})
        return list(cursor)


    def create(self, data):
        """ Create a new data document """
        # if self.exists(data):
        #     self.ns.abort(409, message="document already exists", data={})
        # else:
        data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db.insert(data)
        return {'message': 'success', 'data': data}


    def createMany(self, dataList):
        """ Create multiple data documents"""
        ret = dataList
        # PRE-PROCESS DATA IN LIST
        for data in dataList:
            if self.exists(data):   # avoid duplicates
                ret.remove(data)
            else:
                data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.db.insert_many(ret)
        return ret