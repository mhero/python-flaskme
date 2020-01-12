from flask import Flask, jsonify, Response
from flask_migrate import Migrate
from models import db
from services import UserService

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
migrate = Migrate(app, db)


@app.route('/users')
def users():
    return jsonify(UserService.all())


def create_app(config_name):
    db.init_app(app)
    return app
