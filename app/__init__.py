from flask import Flask, jsonify, Response
from flask_migrate import Migrate
from models import db
from services import UserService
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
migrate = Migrate(app, db)


@app.route('/users')
def users():
    return jsonify(UserService.all())


@app.route("/mp3")
def stream_mp3():
    def generate():
        basedir = os.path.abspath(os.path.dirname(__file__))
        data_file = os.path.join(basedir, 'song.mp3')
        with open(data_file, "rb") as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)
    return Response(generate(), mimetype="audio/x-mp3")


def create_app(config_name):
    db.init_app(app)
    return app
