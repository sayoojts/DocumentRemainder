from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object('config.Config')

mail = Mail(app)

with app.app_context():
    msg = Message(
        'Test Email',
        recipients=['ts1sayooj@gmail.com']
    )
    msg.body = 'This is a test email.'
    try:
        mail.send(msg)
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", e)
