from myapp.database import db
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True, nullable=False)
    password=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)

class Question(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String(200), nullable=False)
    content=db.Column(db.Text(), nullable=False)
    create_date=db.Column(db.DateTime(),nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)           #Ondelete='CASCADE' : user가 삭제되면 question도 삭제됨 (SQLAlchemy에서 지원하는 기능)
    user=db.relationship('User', backref=db.backref('question_set'))#relationship() : User와 Question의 관계를 설정하는 메서드. backref는 User 모델에서 Question 모델을 참조할 수 있도록 해줌.(python에서의 ORM에서 지원하는 기능)
    modify_date=db.Column(db.DateTime(),nullable=True)

class Answer(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    question_id=db.Column(db.Integer, db.ForeignKey('question.id',ondelete='CASCADE'), nullable=False)
    question=db.relationship('Question', backref=db.backref('answer_set'))  
    content=db.Column(db.Text(), nullable=False)
    create_date=db.Column(db.DateTime(),nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)           
    user=db.relationship('User', backref=db.backref('answer_set'))
    modify_date=db.Column(db.DateTime(),nullable=True)
