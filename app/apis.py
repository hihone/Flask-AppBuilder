from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import ModelRestApi

from app import appbuilder
from app.models import BookModel

class BookModelApi(ModelRestApi):
    resource_name = "book"
    datamodel = SQLAInterface(BookModel)

appbuilder.add_api(BookModelApi)