from flask import Flask, render_template

app = Flask(__name__)


with app.app_context():
  from . import db
  db.init_app(app)
 #importo esa y la llamo#



from . import bandas
app.register_blueprint(bandas.bp)


from . import canciones
app.register_blueprint(canciones.bp)


from . import generos
app.register_blueprint(generos.bp)
