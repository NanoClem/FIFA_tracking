from flask_restplus import fields


def create_video_model(ns):
    """ Create a model for a video
    """
    return ns.model('Video', {
        '_id'  : fields.String(decription='Video unique identifier'),
        'path' : fields.String(description='path of the video file')
    })
