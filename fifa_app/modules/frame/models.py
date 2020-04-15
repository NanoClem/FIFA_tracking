from flask_restplus import fields


def create_record_model(ns):
    """ Create a model for a record
    """
    return ns.model('Record', {
        'player_id' : fields.String(description='reference to the player concerned by the record'),
        'position' : fields.Nested( ns.model('Position', {
            'x': fields.Float(description='x-axis coordinate'),
            'y': fields.Float(description='y-axis coordinate')
        }), description='')
    })


def create_frame_model(ns):
    """ Create a model for a frame
    """
    return ns.model('Frame', {
        "_id"       : fields.String(description='unique identifier of the frame'),
        'timestamp' : fields.Integer(description='moment of the frame'),
        'records'   : fields.List(fields.Nested(create_record_model(ns)), description='list of player records in the frame'),   
        'created_at' : fields.String(description='date of creation') 
    })