''' src/__init__.py '''
from flask import Flask
from .views.index import INDEX
from .views.api import API
from .views.admin import ADMIN
from .views.user import USER

# Instance relative config
APP = Flask(__name__, instance_relative_config=True)
APP.config.from_object('config')

# Regist blueprint
APP.register_blueprint(ADMIN, url_prefix='/admin')
APP.register_blueprint(INDEX, url_prefix='/')
APP.register_blueprint(API, url_prefix='/api')
APP.register_blueprint(USER, url_prefix='/user')
