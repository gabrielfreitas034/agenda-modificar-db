from database import db

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  email = db.Column(db.String())
  password = db.Column(db.String())
  created_at = db.Column(db.String())
  updated_at = db.Column(db.String())

class Contacts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  email = db.Column(db.String())
  phone = db.Column(db.String())
  image = db.Column(db.String())
  user_id = db.Column(db.Integer)
  created_at = db.Column(db.String())
  updated_at = db.Column(db.String())
