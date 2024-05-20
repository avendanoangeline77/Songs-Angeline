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
    consulta_canciones = """
           select name from tracks
        """
    consulta_generos = """
           select name from genres
         """
    consulta_bandas = """
          select name from artists 

        """

    base_de_datos = db.get_db()

    resultado = base_de_datos.execute(consulta_canciones)
    lista_de_canciones = resultado.fetchall()

    resultado = base_de_datos.execute(consulta_generos)
    lista_de_generos = resultado.fetchall()

    resultado = base_de_datos.execute(consulta_bandas)
    lista_de_bandas = resultado.fetchall()

    pagina = render_template("songs.html", nombre_canciones = lista_de_canciones, generos=lista_de_generos, bandas = lista_de_bandas)
    return pagina