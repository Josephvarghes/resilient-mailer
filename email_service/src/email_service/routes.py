
from flask import Blueprint, request, redirect, url_for, flash, render_template
from email_service.src.email_service.email_service import email_service
from models import EmailLog 
from extensions import db
import re


email_routes = Blueprint('email_routes', __name__)

# Helper function for email validation
def is_valid_email(email):
    """Validate the format of the email using regex."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Route for rendering the email form
@email_routes.route('/send-email', methods=['GET'])
def send_email_form():
    return render_template('send_email.html')

# Route for handling form submissions
@email_routes.route('/send-email', methods=['POST'])
def send_email_form_submission():
    # Retrieve form data
    to = request.form.get('recipient')
    subject = request.form.get('subject')
    body = request.form.get('body')

    # Validate inputs
    if not to or not subject or not body:
        flash("Please fill out all fields before submitting.", "error")
        return redirect(url_for('email_routes.send_email_form'))

    # Validate email format
    if not is_valid_email(to):
        flash("The recipient email address is invalid. Please provide a valid email.", "error")
        return redirect(url_for('email_routes.send_email_form'))

    # Attempt to send email
    result = email_service.send_email(to, subject, body)

    # Save email details to the database
    email_log = EmailLog(
        recipient=to,
        subject=subject,
        body=body,
        status=result['status'],
        provider=result.get('provider', 'N/A'),  # Optional, depends on your email service
        error=result.get('error')  # Save error details if any
    )
    db.session.add(email_log)
    db.session.commit()

    # Flash appropriate messages
    if result['status'] == 'success':
        flash(f"Email successfully sent to {to}.", "success")
    else:
        flash(f"Failed to send email. Error: {result.get('error', 'Unknown error')}", "error")

    # Redirect to form after submission
    return redirect(url_for('email_routes.send_email_form'))

@email_routes.route('/email-logs', methods=['GET'])
def email_logs():
    logs = EmailLog.query.order_by(EmailLog.timestamp.desc()).all()
    return render_template('email_logs.html', logs=logs)