from flask_restplus import fields


def create_player_model(ns):
    """ Create a model for a player
    """
    return ns.model('Player', {
        '_id'           : fields.String(description='unique identifier of the frame'),
        'team_id'       : fields.String(description='reference to the team to which the player belongs'),
        'role'          : fields.String(description='role played of the field'),
        'jersey_number' : fields.Integer(description='number of the jersey'),
        'first_name'    : fields.String(description='first name of the player'),
        'last_name'     : fields.String(description='last name of the player'),
    })


def create_team_model(ns):
    """ Create a model for a team
    """
    return ns.model('Teams', {
        '_id'          : fields.String(description='The unique identifier of the team'),
        'name'         : fields.String(description='The name of the soccer team'),
        'jersey_color' : fields.String(description='Hex value of the jersey color'),
        'players'      : fields.List(fields.Nested(create_player_model(ns)), description='List of players in the team'),
        'tactic'       : fields.String(description='How the team is positioned of the field'),
        'created_at'   : fields.String(description='Date of creation')
    })