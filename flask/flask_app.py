from flask import Flask
from Glance_flaskBased.views.viewfunctions import *
from Glance_flaskBased.config import *

def creat_flask_app():
    app = Flask(__name__)
    app.config.from_object(devConfig)
    app.add_url_rule('/',view_func=submit_ar)
    return app