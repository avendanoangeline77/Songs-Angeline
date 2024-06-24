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