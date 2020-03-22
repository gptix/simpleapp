# from decouple import config
from flask import Flask, render_template, request

# from .models import DB, User
# from .predict import predict_user
# from .twitter import add_or_update_user, update_all_users


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return True

    return app
