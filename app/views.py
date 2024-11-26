from gettext import gettext
from tkinter.tix import NoteBook

from flask import render_template
from flask_appbuilder.models.sqla.filters import FilterNotEqual
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from wtforms.validators import Length

from app import appbuilder, db
from app.models import BookModel

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


class BookModelView(ModelView):
    datamodel = SQLAInterface(BookModel)

    # 添加页面字段
    add_fieldsets = [(
        '书的信息',
        {'fields': ['title', 'content']}
    )]

    # 编辑页面要填写的字段
    edit_fieldsets = [(
        '书的信息',
        {'fields': ['title', 'content']}
    )]

    # 定义在前端显示时，model的列，显示成一个新别名
    label_columns = {'id': 'ID', 'title': '标题', 'content': '内容', 'create_time': '创建时间'}
    list_columns = ['id', 'title', 'content', 'create_time']

    show_fieldsets = [
        (
            '详情',
            {'fields': ['id', 'title', 'content', 'create_time']}
        )
    ]

    # 定义list页面的默认筛选条件的配置
    base_filters = [['title', FilterNotEqual, ''], ]  # 筛选出名称为''的
    # 定义list页面的排序方法
    base_order = ('id', 'desc')

    search_columns = ['title']

    # 设置排序字段
    order_columns = ['id', 'create_time']

    validators_columns = {
        'title': [Length(min=1, message=gettext('标题不能为空'))],  # message 为错误时的提示消息
        'content': [Length(min=1, message=gettext('内容不能为空'))]  # message 为错误时的提示消息
    }

    page_size = 2


db.create_all()
appbuilder.add_view(BookModelView, "Book 列表", category="日志组",)

