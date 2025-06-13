from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from datetime import timedelta

app = Flask(__name__)

# Konfigurasi CORS
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:5173"],  # Frontend Vite default port
        "methods": ["GET", "POST", "PATCH", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Konfigurasi Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_size": 10,
    "pool_recycle": 3600,
    "pool_pre_ping": True
}

# Konfigurasi Keamanan
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=1)

# Konfigurasi Performa
app.config["JSON_SORT_KEYS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

db = SQLAlchemy(app)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return {"message": "Resource not found", "status": "error"}, 404

@app.errorhandler(500)
def internal_error(error):
    return {"message": "Internal server error", "status": "error"}, 500
