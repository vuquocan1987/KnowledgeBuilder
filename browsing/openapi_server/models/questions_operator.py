from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from openapi_server.config import Config
from openapi_server.models.db import db
from openapi_server.models.db_models import User

def query_question(user_name):
    if user_name:
        return ["question1","question2","question3"]


def signup(user_name,email,password ):
    """Create a new user, and return True if successful, False otherwise"""
    hased_password = generate_password_hash(password, method='sha256')
    new_user = User(username=user_name, email=email, password=hased_password)
    # check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return False
    db.session.add(new_user)
    db.session.commit()
    access_token = create_access_token(identity=user_name)
    return True