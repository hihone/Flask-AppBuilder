- 安装 flask-AppBuilder::

    conda create --name appBuilder-demo

    conda activate appBuilder-demo

    pip install flask-appbuilder


- 生成项目::

    fabmanager create-app

- 创建数据库::

    fabmanager create-admin 

- 运行环境::

    fabmanager run

    swagger 运行配置 config.py

    FAB_API_SWAGGER_UI = True


- 国际化中文::

    # https://flask-appbuilder.readthedocs.io/en/v3.2.0/i18n.html
    pybabel init -i ./babel/messages.pot -d app/translations -l zh

- 国际化编译::

    fabmanager babel-compile 或 flask fab babel-compile