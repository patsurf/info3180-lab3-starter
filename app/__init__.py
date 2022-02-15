from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
#app.config['MAIL_SERVER']='smtp.mailtrap.io'
#app.config['MAIL_PORT'] = 2525
#app.config['MAIL_USERNAME'] = 'ac09cbb0817d18'
#app.config['MAIL_PASSWORD'] = 'c3091e428705ce'
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
from app import views
