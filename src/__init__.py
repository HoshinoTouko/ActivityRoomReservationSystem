''' src/__init__.py '''
from flask import Flask
from .views.index import INDEX
from .views.api import API

# Instance relative config
APP = Flask(__name__, instance_relative_config=True)
APP.config.from_object('config')

# Regist blueprint
APP.register_blueprint(INDEX, url_prefix='/')
APP.register_blueprint(API, url_prefix='/api')
