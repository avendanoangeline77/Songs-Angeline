from flask import Flask, render_template

app = Flask(__name__)


with app.app_context():
  from . import db
  db.init_app(app)
 #importo esa y la llamo#


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/canciones')
def songs():
    base_de_datos = db.get_db()
    consulta = """
        SELECT last_name, first_name FROM actor
        ORDER BY last_name, first_name;
        """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    return render_template("songs.html", songs =lista_de_resultados)