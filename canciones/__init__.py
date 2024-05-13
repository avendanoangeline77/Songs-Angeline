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
    consulta = """
           select g.name as genero, t.name as canciones, a.Title as albuns from genres g
           join tracks t on g.GenreId = t.GenreId
           join albums a on t.AlbumId = a.AlbumId
        """
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("songs.html", songs = lista_de_resultados)
    return pagina