from flask import Flask
from flask import Flask
from .models import db
from .routes import scheduler_bp
import streamlit as st

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///study.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(scheduler_bp)
    return app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
