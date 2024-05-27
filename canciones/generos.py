from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint("generos",__name__, url_prefix="/generos")

@bp.route('/')
def canciones():
    consulta_generos = """
      select name from genres

        """

    base_de_datos = db.get_db()

    resultado = base_de_datos.execute(consulta_generos)
    lista_de_generos = resultado.fetchall()

    pagina = render_template("generos.html",  generos = lista_de_generos)
    return pagina