import os
from flask import Flask,render_template
from email_service.src.email_service.routes import email_routes
from extensions import db

app = Flask(__name__)

app.secret_key = os.urandom(24) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database object
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

# Register routes from the email_service module
app.register_blueprint(email_routes, url_prefix='')

if __name__ == '__main__':
    app.run(debug=True)