from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint("bandas",__name__, url_prefix="/bandas")

@bp.route('/')
def canciones():
    consulta_bandas = """
          select name from artists 

        """

    base_de_datos = db.get_db()

    resultado = base_de_datos.execute(consulta_bandas)
    lista_de_bandas = resultado.fetchall()

    pagina = render_template("bandas.html",  bandas = lista_de_bandas)
    return pagina