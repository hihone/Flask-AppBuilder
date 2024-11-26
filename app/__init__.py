import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

from app.index import MyIndexView

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.debug = True
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView)

from app import views
# from app import books
from app import apis
from app import charts
