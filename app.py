from Models import db
from flask import Flask
from routes.routes import user
from views import user_views


class Config:
   SECRET_KEY="bapan app"
   SQLALCHEMY_DATABASE_URI="postgresql://postgres:36network@localhost/bello"
   SQLALCHEMY_TRACK_MODIFICATIONS=False
    


def create_app():
   app=Flask(__name__)
   app.config.from_object(Config)
   db.init_app(app)
   with app.app_context():
       db.create_all()
   app.register_blueprint(user)
   return app
   


if __name__=="__main__":
   app=create_app()
   app.run(debug=True)