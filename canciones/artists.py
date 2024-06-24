from flask import Blueprint, render_template
from . import db

bp = Blueprint("artists",__name__, url_prefix="/artists")

@bp.route('/<int:id>')
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
    pagina = render_template('detallesCanciones.html',
                             artistas=artistas,
                             canciones = lista_canciones)
    return pagina

@bp.route('/')
def artists():
    data_base = db.get_db()
    ask = """
          select name from artists 
        """
    artists = data_base.execute(ask)
    lista_de_artistas = artists.fetchall()

    pagina = render_template("artistas.html",  artists = lista_de_artistas)

    return pagina
