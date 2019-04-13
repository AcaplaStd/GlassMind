from flask import *
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.routing import Rule

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
app.url_rule_class = lambda path, **options: Rule(app.config['APPLICATION_ROOT'] + '/' + path, **options)
app.wsgi_app = ProxyFix(app.wsgi_app)

from app import routes, models
