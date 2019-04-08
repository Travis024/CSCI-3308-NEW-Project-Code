from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
#from models import User

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# app.config['DEBUG'] = True
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
# %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
# db.init_app(app)

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models



#
# if __name__ == "__main__":
#     app.run()
