from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from .models import Reminder
from .email import send_reminder_email

scheduler = BackgroundScheduler()

def check_and_send_reminders(app):
    print("Inside check and send reminders")
    with app.app_context():
        reminders = Reminder.query.all()
        for reminder in reminders:
            if reminder.due_date - timedelta(days=5) <= datetime.utcnow() <= reminder.due_date:
                send_reminder_email(reminder)

def start_scheduler(app):
    scheduler.add_job(func=check_and_send_reminders, args=[app], trigger="interval", minutes=1)
    scheduler.start()

def shutdown_scheduler():
    scheduler.shutdown()
