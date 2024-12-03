from flask import Flask
from email_service.src.email_service.routes import email_routes

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Resilient Mailer API! Use `/api/send` to test." 

# Register routes from the email_service module
app.register_blueprint(email_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)