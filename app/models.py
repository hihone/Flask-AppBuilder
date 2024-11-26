from datetime import datetime
import random

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Text, DateTime

from app import db

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class BookModel(Model):
    __tablename__ = 'ab_book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False)

    def __init__(self):
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def rand_count(self):
        return random.randint(1, 100)

    def rand_count1(self):
        return random.randint(1, 100)

    def __repr__(self):
        return f'title:{self.title}, content: {self.content}'


db.create_all()