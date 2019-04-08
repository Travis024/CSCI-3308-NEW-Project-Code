from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column('user_id',db.Integer, primary_key=True)
    firstName = db.Column('firstName', db.String)
    lastName = db.Column('lastName', db.String)
    email = db.Column('email', db.String, unique=True)
    username = db.Column('username', db.String, unique=True)
    password = db.Column('password', db.String, nullable=False)

    def __init__(self, firstName, lastName, email,
                username, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % (self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
