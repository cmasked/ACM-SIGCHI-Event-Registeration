from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = '8e43a8237aa2469efcbcd0e173fced6f'

csrf = CSRFProtect(app)

from event import routes

