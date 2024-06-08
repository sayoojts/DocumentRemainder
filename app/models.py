from . import db

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document_name = db.Column(db.String(120), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_email = db.Column(db.String(120), nullable=False)
