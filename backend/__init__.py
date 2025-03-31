from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Import routes after app initialization to avoid circular imports
from backend import routes 
