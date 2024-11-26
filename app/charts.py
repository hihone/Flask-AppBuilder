from flask_appbuilder import DirectByChartView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from app import appbuilder
from app.models import BookModel


class BookDirectChart(DirectByChartView):
    datamodel = SQLAInterface(BookModel)

    chart_title = '书籍信息'
    chart_type = 'ColumnChart' # PieChart(饼图) ColumnChart(竖状图) LineChart(线形图)

    search_columns = ['title']

    # 定义报表部分前端页面的相关显示。多个图表，每个图表包含多个曲线数据。
    definitions = [
        {
            'label': 'book',  # 当前图表的标题
            'group': 'title',  # 用来作为x的字段。
            'series': ['rand_count', 'rand_count1']  # 用来作为y的字段，包含多个y值
        }
    ]


appbuilder.add_view(BookDirectChart, "Book Chart", category="Charts")