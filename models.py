from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
