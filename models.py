from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, false, null

db = SQLAlchemy()

class Users(db.Model):
    username = db.Column(db.String, nullable = False)
    passcode = db.Column(db.String, nullable = False)
    users_id = db.Column(db.Integer, primary_key = True)
    
    # post_id=db.relationship("Posts",backref="users")

    def __repr__(self):
        return f'Users({self.username}, {self.passcode}, {self.users_id})'


class Posts(db.Model):
    post_id= db.Column(db.String,primary_key=True)
    post_title=db.Column(db.String,nullable=False)
    post_comment=db.Column(db.String,nullable=False)
    # user_id=db.Column(db.Integer,db.ForeignKey("users.users_id"))
    def __repr__(self):
        return f'Posts({self.post_id}, {self.post_title}, {self.post_comment})'
