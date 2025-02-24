from importlib import import_module

from flask import Flask
from flask_socketio import SocketIO

from app.core.socket import DockerSocket
from app.database import Base, engine
from app.config import Config

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)

    register_blueprints(app)
    
    # Base.metadata.create_all(bind=engine)

    return app

def create_socketio(app):
    global socketio_instance

    socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet', engineio_logger=True)
    socketio.on_namespace(DockerSocket('/docker',socketio_instance=socketio))

    return socketio

def register_blueprints(app):
    for module_name in ('auth', 'home'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)