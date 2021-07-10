from alert.app import db

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    uid = db.Column(db.String(40))
    latitude = db.Column(db.String(40))
    longitude = db.Column(db.String(40))
    date = db.Column(db.Date)