from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medio

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

'''prueba
with app.app_context():
    c = Cancion(titulo='Prueba', minutos=2, segundos=25, interprete='Carlos')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())'''
with app.app_context():
    c = Cancion(titulo='si', minutos=3, segundos=20, interprete='Arcangel')
    u = Usuario(nombre='sebastian', contrasena='password')
    a = Album(titulo='prueba', anio=2000, description='Maravilla', medio=Medio.CD)
    a.canciones.append(c)
    u.albumes.append(a)
    db.session.add(a)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    db.session.delete(u)
    print(Usuario.query.all())
    print(Album.query.all())
    print(Cancion.query.all())
