from flask import Flask, render_template, request

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "Did not crash"

    return app
