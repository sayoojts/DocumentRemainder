from flask_mail import Message
from flask import current_app as app
from . import mail

def send_reminder_email(reminder):
    msg = Message(
        'Document Reminder',
        sender='noreply@demo.com',
        recipients=[reminder.user_email]
    )
    msg.body = f'Reminder: Your document {reminder.document_name} is due on {reminder.due_date.strftime("%Y-%m-%d")}.'
    mail.send(msg)
