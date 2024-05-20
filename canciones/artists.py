from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint("artists",__name__, url_prefix="/tipos_canciones")

@bp.route('/')
def hello():
    return 'Hello, World!'

@bp.route('/<init:id>')
def canciones(id):
    consulta_canciones = """
            select name from tracks
            where GenreId = ?;        
            """
    consulta_generos = """
           select .name from genres g join tracks t on t.GenreId = g.GenreId where g.GenreId = ?; 
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