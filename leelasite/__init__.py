import os
from flask import Flask
from . import db
from . import routes

def create_app(test_config=None):
    app = Flask (__name__, template_folder='../templates', static_folder='../static')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'leelasite.sqlite'),
    )
    print(app.instance_path)
    app.register_blueprint(routes.bp)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)
    return app