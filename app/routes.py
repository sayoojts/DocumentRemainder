from flask import render_template, request, redirect, url_for, current_app as app
from app import db
from app.models import Reminder
from datetime import datetime

@app.route('/')
def index():
    reminders = Reminder.query.all()
    return render_template('index.html', reminders=reminders)

@app.route('/add', methods=['POST'])
def add_reminder():
    document_name = request.form['document_name']
    due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
    user_email = request.form['user_email']  # Ensure to capture user_email from the form
    reminder = Reminder(document_name=document_name, due_date=due_date, user_email=user_email)
    db.session.add(reminder)
    db.session.commit()
    return redirect(url_for('index'))
