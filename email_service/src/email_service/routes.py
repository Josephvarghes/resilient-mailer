from flask import Blueprint, request, jsonify
from email_service.src.email_service.email_service import email_service
email_routes = Blueprint('email_routes', __name__)



@email_routes.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    to = data.get('to')
    subject = data.get('subject')
    body = data.get('body')
    
    if not to or not subject or not body:
        return jsonify({"status": "failed", "message": "Missing required fields"}), 400
    
    result = email_service.send_email(to, subject, body)
    return jsonify(result)
    