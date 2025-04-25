from datetime import datetime
from flask import Blueprint, render_template, request, redirect, current_app, g, url_for, flash
from werkzeug.utils import redirect
from myapp.models import Question, Answer, User
from myapp.database import db
from myapp.forms import AnswerForm

bp=Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>/', methods=('POST',))
def create(question_id):
    question=Question.query.get_or_404(question_id)
    content= request.form['content']
    annoymous_user= User.query.filter_by(username='testuser').first()
    #user=g.user if g.user else annoymous_user

    current_app.logger.info('annonymous_user:',annoymous_user)

    answer=Answer(content=content, create_date=datetime.now(),user=annoymous_user)
    question.answer_set.append(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question.id))    

@bp.route('/modify/<int:answer_id>/', methods=('GET', 'POST'))
def modify(answer_id):
    current_app.logger.info('modify:',answer_id)
    answer=Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정 권한이 없습니다.')  
        return redirect(url_for('question.detail', question_id=answer.question.id))
    if request.method=='POST':
        form=AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date=datetime.now()
            db.session.commit()
            return redirect(url_for('question.detail', question_id=answer.question.id))
    else:
            form=AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', form=form)
    
@bp.route('/delete/<int:answer_id>/')
def delete(answer_id):
    current_app.logger.info('delete:',answer_id)    
    answer=Answer.query.get_or_404(answer_id)
    question_id=answer.question.id
    if g.user != answer.user:
        flash('삭제 권한이 없습니다.')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))    