from flask_restplus import fields



# TEAM MODEL
def create_team_model(ns):
    """ Creates fields for the crypto model

    Returns
    -----
    (dict) : fields of the crypto model
    """
    model = ns.model("Teams", {
        "_id"        : fields.String(description="The unique identifier of the team"),
        "name"       : fields.String(required=True, description="The name of the soccer team"),
        "created_at" : fields.String(required=True, description="Timestamp of creation")
    })

    return model



# RECORD MODEL
def create_record_model(ns):
    """
    """
    # AXIS
    positions_fields = ns.model("Position", {
        "x" : fields.Float(description="the x_axis of the position"),
        "y" : fields.Float(description="the y_axis of the position"),
    })

    # TEAMS
    teams_fields = ns.model("Nested_team", {
        "team_id"   : fields.String(description="A reference of the team by its id"),
        "positions" : fields.List(fields.Nested(positions_fields))
    })

    # RECORDS
    model = ns.model("Record", {
        "_id"        : fields.String(description="The unique identifier of the record"),
        "timestamp"  : fields.Integer(required=True, description="Time of the video at when the record is made"),
        "created_at" : fields.String(required=True, description="Timestamp of creation"),
        "teams"      : fields.List(fields.Nested(teams_fields))
    })

    return model