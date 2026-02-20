#!/usr/bin/env python3
"""
API Security and Authentication Techniques
- Basic Authentication with Flask-HTTPAuth
- JWT Authentication with Flask-JWT-Extended
- Role-based Access Control
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)

# Strong secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user store
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ==============================
# BASIC AUTHENTICATION
# ==============================

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


# ==============================
# JWT ERROR HANDLERS (ALL 401)
# ==============================

@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_fresh_token_required(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# ==============================
# JWT LOGIN
# ==============================

@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad username or password"}), 401

    # Embed role inside JWT identity
    access_token = create_access_token(
        identity={"username": username, "role": user["role"]}
    )

    return jsonify(access_token=access_token), 200


# ==============================
# JWT PROTECTED ROUTE
# ==============================

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


# ==============================
# ROLE-BASED ACCESS CONTROL
# ==============================

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()

    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"}), 200


# ==============================
# RUN APP
# ==============================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
