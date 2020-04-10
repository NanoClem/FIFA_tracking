from flask_restplus import fields
from ..player.models import create_player_model


# COLOR MODEL
def create_color_model(ns):
    """ Create a model for a color
    """
    return ns.model('HSV', {
        'h'          : fields.Integer(required=True),
        's'          : fields.Integer(required=True),
        'v'          : fields.Integer(required=True),
    })


# JERSEY MODEL
def create_jersey_model(ns):
    """ Create a model for a jersey
    """
    return ns.model('Jersey', {
        'color'      : fields.List(fields.Nested(create_color_model(ns)), required=True, description='Color range of the jersey'),
        'home'       : fields.Boolean(required=True, description='Tells if either it is the home jersey or not'),
    })


# TEAM MODEL
def create_team_model(ns):
    """ Create a model for a team
    """
    return ns.model('Teams', {
        '_id'               : fields.String(description='The unique identifier of the team'),
        'name'              : fields.String(description='The name of the soccer team'),
        'players'           : fields.List(fields.Nested(create_player_model(ns)), description='List of players in the team'),
        'jersey'            : fields.Nested(create_jersey_model(ns), description='Information about the jersey of the team'),
        'goalkeeper_jersey' : fields.Nested(create_jersey_model(ns), description='Information about the jersey of the goalkeeper'),
        'tactic'            : fields.String(description='How the team is positioned of the field'),
        'created_at'        : fields.String(description='Date of creation')
    })