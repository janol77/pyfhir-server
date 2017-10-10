from flask import Flask
from flask_restful import Api
from load_resources import find_resources
from resources.Test.test_controller import *
import json


def create_app(config_file="config.json"):
    app = Flask(__name__)
    with open(config_file, 'r') as f:
        config = json.load(f)
        app.config.update(config)
    db_type = app.config.get('DB_TYPE', 'MONGO')
    if db_type == 'MONGO':
        from db import db
        db.init_app(app)
    else:
        from flask_sqlalchemy import SQLAlchemy
        db = SQLAlchemy(app)
    find_resources(app)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(host=app.config.get('HOST', '0.0.0.0'),
            port=app.config.get('PORT', 5000),
            debug=app.config.get('DEBUG', False)
            )
