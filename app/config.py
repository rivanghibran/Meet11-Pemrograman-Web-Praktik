import os

class config:
    SQLACHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLACHEMY_TRACK_MODIFCATIONS = False