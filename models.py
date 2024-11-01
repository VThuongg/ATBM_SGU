from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    public_key = db.Column(db.String, nullable=False)
    private_key = db.Column(db.String, nullable=False)

class EncryptedEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    aes_key = db.Column(db.Text, nullable=False)
    signature = db.Column(db.Text, nullable=False)
    attachment = db.Column(db.String(255), nullable=True)  # Add this line
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    encrypted_attachment_content = db.Column(db.Text, nullable=True)
    # image = db.Column(db.String, nullable=True)  # Add this line for image support