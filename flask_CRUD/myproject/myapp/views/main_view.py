from flask import Blueprint, render_template,current_app,url_for
from myapp.models import Question
from werkzeug.utils import redirect # redirect는 URL을 리다이렉트하는 함수

bp=Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    # question_list=Question.query.order_by(Question.create_date.desc())
    # 질문 목록을 최신순으로 정렬하여 가져옴
    current_app.logger.info('메인페이지 접근')
    # return render_template('question/question_list.html',
    # question_list=question_list)  # question_list.html 템플릿에 질문 목록을 전달
    return redirect(url_for('question.qlist'))


# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question=Question.query.get(question_id)
#     current_app.logger.info('detail페이지 접근')
#     return render_template('question/question_detail.html',question=question)





# @bp.route('/hello')
# def hello():
#     return 'Hello hello page!'  

# @bp.route('/<id>')
# def index_id(id):
#     return render_template('index.html',
#     title="나의 홈피", username=id)
