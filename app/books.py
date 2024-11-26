from flask import request, jsonify, redirect
from flask_appbuilder import BaseView, expose

from app import appbuilder, db
from app.models import BookModel


class bookView(BaseView):
    route_base = '/book'

    default_view = 'book_list'
    @expose('/list', methods=['GET'])
    def book_list(self):
        session = db.session
        books = session.query(BookModel).order_by(BookModel.id.desc()).all()
        return self.render_template('books/list.html', books=books)

    @expose('/add', methods=['POST', 'GET'])
    def add(self):
        if request.method == 'GET':
            return self.render_template('books/add.html')
        title = request.form.get('title')
        if not title:
            return jsonify(code=1, message="请输入日志名称")
        content = request.form.get('content')
        if not content:
            return jsonify(code=1, message="请输入日志内容")
        session = db.session
        book = BookModel()
        book.title = title
        book.content = content
        session.add(book)
        session.commit()

        return redirect('/book/list')


appbuilder.add_view(bookView, "Book 列表", category="日志组")
appbuilder.add_link("Book 添加", href="/book/add", category="日志组")