from flask import jsonify
from Models import db
from Models.user_models import User
from routes.routes import user
from flask import request

@user.route('/users',methods=['GET'])
def get_all_users():
   user_list=list()
   users=User.query.all()
   for user in users:
      myuser=dict()
      myuser.update(name=user.name)
      myuser.update(email=user.email)
      myuser.update(id=user.id)
      user_list.append(myuser)
   return jsonify(user_list)


@user.route('/users',methods=['POST'])
def create_user():
   user=request.get_json()
   new_user=User(name=user.get("name",'XX'),email=user.get("email",'a@b.com'))
   db.session.add(new_user)
   db.session.commit()
   db.session.refresh(new_user)
   user.update(id=new_user.id)
   return jsonify(user)
   
   
   