from flask import Flask
import os

from application_factory import db


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'application_factory.sqlite')
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping()

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        print('error===', str(e))

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Welcome, World!'

    db.init_app(app)
    return app
