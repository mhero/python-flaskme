from flask_login import UserMixin
from marshmallow import Schema, fields
from models import db
import datetime


class User(UserMixin, db.Model):
    """
    Create a User table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    created_ts = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name=None, created_ts=None):
        self.name = name
        self.value_me = created_ts

    def __repr__(self):
        return '<Object %r %r>' % (self.id, self.name, self.created_ts)


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    created_ts = fields.Date()
