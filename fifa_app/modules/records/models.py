from flask_restplus import fields


# POSITION MODEL
def create_position_model(ns):
    """
    """
    positions_model = ns.model("Position", {
        "x" : fields.Float(required=True, description="the x_axis of the position"),
        "y" : fields.Float(required=True, description="the y_axis of the position"),
    })
    return positions_model



# RECORD TEAMS MODEL
def create_teamsRecord_model(ns):
    """
    """
    teamsRecord_model = ns.model("TeamsRecord", {
        "team_id"   : fields.String(required=True, description="A reference of the team by its id"),
        "positions" : fields.List(fields.Nested(create_position_model(ns)), required=True)
    })
    return teamsRecord_model



# RECORD MODEL
def create_record_model(ns):
    """
    """
    record_model = ns.model("Record", {
        "_id"        : fields.String(description="The unique identifier of the record"),
        "timestamp"  : fields.Integer(required=True, description="Time of the video at when the record is made"),
        "created_at" : fields.String(required=True, description="Date of creation"),
        "teams"      : fields.List(fields.Nested(create_teamsRecord_model(ns)), required=True)
    })
    return record_model