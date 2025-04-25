from flask import Flask
import config
from myapp.database import db, migrate  # database.py에서 db와 migrate를 가져옴
import os

import logging
from logging.handlers import RotatingFileHandler # 로그를 파일로 저장하기 위한 핸들러

def create_app(): # app을 전역변수로 사용할 필요가 없으므로 create_app()함수로 감싸줌
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG') # 환경변수에서 설정을 가져옴
    #app.config.from_object(config)  # config.py에서 설정을 가져옴

    db.init_app(app)  # Flask 앱에 SQLAlchemy 초기화
    migrate.init_app(app, db)  # Flask 앱에 Flask-Migrate 초기화

    from . import models  # models.py에서 모델을 가져옴(#.은 현재 디렉토리를 의미함 =myapp)
    from .views import main_view, auth_view,board_view, question_view, answer_view, sql_view # __init__.py에서 main_view를 import하여 사용

    app.register_blueprint(main_view.bp)
    app.register_blueprint(auth_view.bp)
    app.register_blueprint(board_view.bp)
    app.register_blueprint(question_view.bp)
    app.register_blueprint(answer_view.bp)
    #app.register_blueprint(sql_view.bp)

    if not os.path.exists('logs'):
        os.makedirs('logs')  # logs 디렉토리가 없으면 생성

    log_file = RotatingFileHandler('logs/myapp.log', maxBytes=1024*1024*10, backupCount=10, encoding='utf-8') # 로그 파일을 10MB로 설정하고, 최대 10개까지 백업
    log_file.setLevel(logging.DEBUG)  # 로그 레벨을 DEBUG로 설정

    app.logger.addHandler(log_file)  # Flask 앱의 로거에 핸들러 추가
    app.logger.setLevel(logging.DEBUG)  # Flask 앱의 로거 레벨을 DEBUG로 설정
    app.logger.info('앱이 구동되었음')  # 앱 시작 로그 기록

    return app

# @app.route('/')
# @app.route('/home/')
# @app.route('/index/')
# def index():
#     return 'Hello index page!'

# @app.route('/about/')
# def about():
#     return '회사소개'

# @app.route('/contact/')
# def contact():
#     return '연락처'

# @app.route('/login/')
# def login():
#     return '아이디와 비번으로 로그인'

# @app.route('/board/')
# def board():
#     return '게시판'

# @app.route('/board/<id>')
# def board_id(id):
#     return f'게시판 글 : {id}'