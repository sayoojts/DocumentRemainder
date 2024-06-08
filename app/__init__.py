from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    with app.app_context():
        from app import routes, models  # Import routes and models within app context
        from app.scheduler import start_scheduler
        start_scheduler(app)  # Start the scheduler with the app

    return app
