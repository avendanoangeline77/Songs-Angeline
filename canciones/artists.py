from flask import Blueprint, render_template,request,url_for,redirect
from . import db

bp = Blueprint("artists",__name__, url_prefix="/artists")

@bp.route('/<int:id>')
def detalles(id):
    con= db.get_db()
    consulta1 = """
      SELECT name, ArtistId FROM artists WHERE  ArtistId = ?;
    """
    consulta2 = """
    SELECT Title, AlbumId FROM albums WHERE ArtistId = ?; 
    """
    res = con.execute(consulta1, (id,))
    artista = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_albums = res.fetchall()
    pagina = render_template('detallesArtistas.html',
                             artista=artista,
                             albums = lista_albums)
    return pagina

@bp.route('/')
def artists():
    data_base = db.get_db()
    ask = """
          select name, ArtistId from artists 
        """
    artists = data_base.execute(ask)
    lista_de_artistas = artists.fetchall()

    pagina = render_template("artistas.html",  artists = lista_de_artistas)

    return pagina

@bp.route('/new', methods=('GET', 'POST'))
def nuevo():
   if request.method == 'POST':
       name = request.form["Name"]

       con = db.get_db() 
       consulta = """ INSERT INTO artists(Name)
                       VALUES (?)
       """
       con.execute(consulta, (name,))
       con.commit()
       return redirect(url_for('artists.artists'))


   else:
    pagina = render_template('nuevoArtista.html')
    return pagina 