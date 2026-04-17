# app/__init__.py

from flask import Flask
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tendencias:Tendencias*2026!@212.85.2.90:5433/clase_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    return app