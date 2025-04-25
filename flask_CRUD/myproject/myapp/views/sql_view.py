from flask import Blueprint, abort
from myapp.database import db
from myapp.models import User, Question, Answer
from datetime import datetime

bp=Blueprint('sql', __name__, url_prefix='/sql')

@bp.route('/create_user/')
def create_user():
    user=User(username='testuser', password='1111',email='test@example.com')
    db.session.add(user)
    db.session.commit()
    return 'User 생성 완료'

@bp.route('/create/')
def create():
    user=User.query.filter_by(username='testuser').first()
    if user is None:
        abort(404, description="해당 사용자를 찾을 수 없습니다.")  # user가 없으면 404 에러 발생

    q=Question(subject='첫번째 질문', 
             content='첫번째 질문입니다..', 
             create_date=datetime.now(),
             user= user)
    db.session.add(q)
    db.session.commit()
    return f'{q.id}번 질문을 등록했습니다.'

@bp.route('/read/')
def read():
    question=Question.query.all()
    #question=Question.query.filter_by # filter_by()는 조건에 맞는 데이터만 가져오는 메서드
    result=''
    for q in question:
        result += f'{q.id}번 질문: {q.subject} <br>'
    return result   

@bp.route('/update/')
def update():
    q=Question.query.get(2)  # id가 1인 질문을 가져옴
    if q is None:
        abort(404, description="해당 질문을 찾을 수 없습니다.")
    q.subject='수정된 질문입니다.'
    q.modify_date=datetime.now()  # 수정일시를 현재시간으로 설정
    db.session.commit()  # 변경사항을 DB에 반영  
    return '질문이 수정되었습니다.'


@bp.route('/delete/')
def delete():
    q=Question.query.get(4)  # id가 1인 질문을 가져옴
    if q is None:
        abort(404, description="해당 질문을 찾을 수 없습니다.")
    db.session.delete(q)
    db.session.commit()

    return '질문이 삭제되었습니다.'

@bp.route('/create_answer/')
def create_answer():
    user=User.query.filter_by(username='testuser').first()
    question=Question.query.first()
    if user is None or question is None:
        abort(404, description="해당 사용자를 찾을 수 없습니다.")  # user가 없으면 404 에러 발생
    a=Answer(content='이렇게 답변하는게 맞는지 모르겠네요..', 
             create_date=datetime.now(),
             question=question,
             user= user)
    db.session.add(a)
    db.session.commit()
    return '질문을 등록했습니다.'