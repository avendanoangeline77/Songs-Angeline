from flask import Flask

app = Flask(__name__)


with app.app_context():
  from db import init_app
  init_app(app)
 #importo esa y la llamo#


@app.route('/')
def hello():
    return 'Hello, World!'