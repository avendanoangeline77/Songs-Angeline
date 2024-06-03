from flask import Blueprint, render_template
from . import db

bp = Blueprint("bandas",__name__, url_prefix="/bandas")

@bp.route('/<init:id>')
def detalles(id):
    con= db.get_db()
    consulta1 = """
      SELECT name FROM artists WHERE  ArtistId = ?;
    """
    consulta2 = """
    SELECT Title, AlbumId FROM albums WHERE ArtistId = ?; 
    """
    res = con.execute(consulta1, (id,))
    artistas = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_canciones = res.fetchall()
    pagina = render_template('detallesCanciones.html'
                             artistas=artistas,
                             canciones = lista_canciones)
    return pagina

@bp.route('/')
def artists():
    data_base = db.get_db()
    ask = """
          select name from artists 
        """
    bandas = data_base.execute(ask)
    lista_de_bandas = bandas.fetchall()

    pagina = render_template("bandas.html",  bandas = lista_de_bandas)