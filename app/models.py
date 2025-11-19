from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="user")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.password_hash, pw)

class Salary(db.Model):
    __tablename__ = 'salary'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    MembershipType = db.Column(db.String(50), nullable=True)
    Rate = db.Column(db.Float, nullable=False)
    HoursWork = db.Column(db.Integer, nullable=True)
    NetPay = db.Column(db.Float, nullable=False)
    deductions = db.Column(db.Float, nullable=False)
    def __repr__(self):
        return f"<Salary {self.name}>"