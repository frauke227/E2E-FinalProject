from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from mongoengine.fields import IntField
from wtforms.fields.core import StringField
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.objects.get(id=user_id)


class User(db.Document, UserMixin):
    #id = db.Column(db.Integer, primary_key=True)
    username = db.StringField(unique=True, nullable=False)
    email = db.EmailField(unique=True, nullable=False)
    image_file = db.StringField(nullable=False,
                           default='default.jpg')
    password = db.StringField(nullable=False)
    account_type=db.StringField()
    posts = db.ReferenceField('Profile', backref='author')

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': str(self.id)}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.objects.get(id=user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Profile(db.Document):
    #id = db.Column(db.Integer, primary_key=True)
    name = db.StringField(nullable=False)
    date_posted = db.DateField(nullable=False,
                            default=datetime.utcnow)
    languages = db.ListField(default=[])
    specialisation = db.StringField(nullable=False)
    address = db.StringField(nullable=False)
    location = db.PointField()
    phone = db.StringField()
    email = db.EmailField()
    website = db.StringField()
    rating = db.ReferenceField('Rating')
    user_id = db.ReferenceField('User')
    views = db.IntField(default=0)
    image_file = db.StringField(nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Language(db.Document):
    language = db.StringField(unique=True, nullable=False)

    def __repr__(self):
        return f"Language('{self.language}')"

class Address(db.Document):
    name = db.StringField(nullable=False)
    address = db.StringField(nullable=False)
    location = db.PointField()
    user_id = db.ReferenceField('User')

    def __repr__(self):
        return f"Post('{self.name}', '{self.address}')"




class Rating(db.Document):
    rating = db.IntField()
    comment = db.StringField()
    user_id = db.ReferenceField('User')
    profile_id = db.ReferenceField('Profile')

    def __repr__(self):
        return f"Rating('{self.rating}', '{self.comment}')"
