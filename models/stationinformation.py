import mongoengine as db

class StationInformation(db.Document):
    station_id = db.StringField(required=True)
    name = db.StringField(required=True)
    coords = db.PointField(required=True)
    capacity = db.IntField(required=True)
    
    meta = {
        'collection': 'stationInformation'
    }