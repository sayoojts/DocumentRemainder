import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reminders.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    #MAIL_USERNAME = 'DocsRemainder@gmail.com'
    #MAIL_PASSWORD = 'Password@87'


    #MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    #MAIL_DEFAULT_SENDER = 'DocsRemainder@gmail.com'

    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'sayoojts87@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'znhg lryk vtjt rony')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'sayoojts87@gmail.com')
