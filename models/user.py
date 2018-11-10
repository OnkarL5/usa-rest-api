from db import db
from werkzeug.security import generate_password_hash
#changed
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    profilePic = db.Column(db.String(150))
    pincode = db.Column(db.Integer)
    password = db.Column(db.String(500))

    def __init__(self, username, firstName, lastName, email, phone, profilePic, pincode, password):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.profilePic = profilePic
        self.pincode = pincode
        self.password = generate_password_hash(password, method='sha256')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() 

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def json(self):
        return {'username': self.username, 'firstName': self.firstName, 'lastName': self.lastName, 'email': self.email, 'phone': self.phone, 'profilePic': self.profilePic, 'pincode': self.pincode}
