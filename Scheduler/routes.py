from flask import Blueprint, render_template, request, redirect, jsonify
from .models import db, Subject
from .utils import generate_schedule

scheduler_bp = Blueprint('scheduler', __name__)

@scheduler_bp.route('/')
def index():
    subjects = Subject.query.all()
    return render_template('index.html', subjects=subjects)

@scheduler_bp.route('/add', methods=['POST'])
def add_subject():
    subject = request.form['subject']
    hours = int(request.form['hours'])
    new_subject = Subject(subject=subject, hours=hours)
    db.session.add(new_subject)
    db.session.commit()
    return redirect('/')

@scheduler_bp.route('/plan')
def show_schedule():
    days = int(request.args.get('days', 5))
    hours = int(request.args.get('hours', 6))
    subjects = Subject.query.all()
    
    if not subjects:
        return "No subjects found!"
    
    schedule = generate_schedule(subjects, days, hours)
    return jsonify(schedule)
@scheduler_bp.route('/delete/<int:id>', methods=['POST'])
def delete_subject(id):
    from .models import Subject
    subject = Subject.query.get_or_404(id)
    db.session.delete(subject)
    db.session.commit()
    return jsonify({"message": "Subject deleted!"})
