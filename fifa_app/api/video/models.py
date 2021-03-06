from flask_restplus import fields


def create_video_model(ns):
    """ Create a model for a video
    """
    return ns.model('Video', {
        '_id'  : fields.String(decription='video unique identifier'),
        'path' : fields.String(description='path of the video file'),
        'title': fields.String(description='title of the video'),
        'teams': fields.List(fields.String(), description='ids of teams involved in the match')
    })
