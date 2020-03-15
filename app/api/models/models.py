from flask_restplus import fields



#------------------------------------------------------------------------------------------------
#     MODELS FOR TEAM DATA
#------------------------------------------------------------------------------------------------

# COLOR MODEL
def create_color_model(ns):
    """
    """
    color = ns.model("RGB", {
        "r" : fields.Integer(required=True),
        "g" : fields.Integer(required=True),
        "b" : fields.Integer(required=True)
    })
    return color



# JERSEY MODEL
def create_jersey_model(ns):
    """
    """
    jersey_model = ns.model("Jersey", {
        "color" : fields.List(fields.Nested(create_color_model(ns)), required=True, description="Color range of the jersey"),
        "home"  : fields.Boolean(required=True, description="Tells if either it is the home jersey or not")
    })
    return jersey_model



# PLAYER MODEL
def create_player_model(ns):
    """
    """
    player_model = ns.model("Player", {
        "last_name"     : fields.String(required=True, description="Last name of the player"),
        "first_name"    : fields.String(required=True, description="First name of the player"),
        "role"          : fields.String(required=True, decription="Player's role on the field"),
        "jersey_number" : fields.Integer(required=True, description="Player's jersey number")
    })
    return player_model



# TEAM MODEL
def create_team_model(ns):
    """
    """
    team_model = ns.model("Teams", {
        "_id"               : fields.String(description="The unique identifier of the team"),
        "name"              : fields.String(required=True, description="The name of the soccer team"),
        "players"           : fields.List(create_player_model(ns), required=True, description="List of the team's players"),
        "jersey"            : fields.Nested(create_jersey_model(ns), required=True, description="Information about the jersey of the team"),
        "goalkeeper_jersey" : fields.Nested(create_jersey_model(ns), required=True, description="Information about the jersey of the goalkeeper"),
        "tactic"            : fields.String(required=True, description="How the team is positioned of the field"),
        "created_at"        : fields.String(required=True, description="Date of creation")
    })
    return team_model




#------------------------------------------------------------------------------------------------
#     MODELS FOR RECORD DATA
#------------------------------------------------------------------------------------------------


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