from flask import Flask
from flask_cors import CORS
from backend import app
import backend.routes  # Ensure this imports your routes

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
