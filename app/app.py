from flask import Flask


def create_app():
    from main import main as main_blueprint
    from api import api as api_blueprint

    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix="/api")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")