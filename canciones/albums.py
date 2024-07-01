from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint("albums",__name__, url_prefix="/albums")

@bp.route('/')
def canciones():
    consulta_albums = """
      select name from albums

        """

    base_de_datos = db.get_db()

    resultado = base_de_datos.execute(consulta_albums)
    lista_de_albums = resultado.fetchall()

    pagina = render_template("album.html",  albums = lista_de_albums)
    return pagina

@bp.route('/<int:id>')
def detalles(id): 
     consulta_albums = """
      select Title from albums
       WHERE AlbumId = ?
     """
     consulta_detalle_albums = """
       select t.Name, a.Title from albums a
       JOIN tracks t on a.AlbumId = t.AlbumId
       WHERE a.AlbumId = ? ;
     """

     base_de_datos = db.get_db()
     resultado = base_de_datos.execute(consulta_albums, (id,))
     albums = resultado.fetchall()

     base_de_datos = db.get_db()
     resultado = base_de_datos.execute(consulta_detalle_albums, (id,))
     lista_de_albums = resultado.fetchall()

     pagina = render_template("detalleAlbums.html", album = albums, albums = lista_de_albums)
     return pagina