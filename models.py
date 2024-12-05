from datetime import datetime
# from app import db  # Import db from app.py
from extensions import db
# EmailLog model for storing email details
class EmailLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    body = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    provider = db.Column(db.String(50), nullable=False)
    error = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, recipient, subject, body, status, provider, error=None):
        self.recipient = recipient
        self.subject = subject 
        self.body = body
        self.status = status
        self.provider = provider
        self.error = error

    def __repr__(self):
        return f'<EmailLog {self.id} - {self.recipient} - {self.status}>'
