from Models import db

class User(db.Model):
  __tablename__="myuser"
  id=db.Column(db.Integer,autoincrement=True,primary_key=True,nullable=False)
  name=db.Column(db.String(20),nullable=False)
  email=db.Column(db.String(30),nullable=False)

  def __init__(self,name,email):
     self.name=name
     self.email=email

  def __str__(self):
     return f"{self.email} and {self.name}"