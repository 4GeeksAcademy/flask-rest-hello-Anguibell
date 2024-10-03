from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Date, index=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __init__ (self, name, lastname, username, email, password, date):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.date = date 
        self.is_active = True

    def __repr__(self):
        return '<Usuario %r>' % self.username
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email,
            "date": self.date,
            # do not serialize the password, its a security breach
        }

class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    #planeta_origen = db.Column(db.Integer, db.ForeignKey("planeta.id"))
    altura = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    unidades_peso = db.Column(db.String(250), nullable=False)
    unidades_altura = db.Column(db.String(250), nullable=False)

    def __init__(self, name, planeta_origen, altura, peso, unidades_peso, unidades_altura):
        self.name = name
        self.planeta_origen = planeta_origen
        self.altura = altura
        self.peso = peso
        self.unidades_peso = unidades_peso
        self.unidades_altura = unidades_altura

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "planeta_origen": self.planeta_origen,
            "altura": self.altura,
            "peso": self.peso,
            "unidades_peso": self.unidades_peso,
            "unidades_altura": self.unidades_altura,
        }

class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    clima = db.Column(db.String(250), nullable=False)
    poblacion = db.Column(db.Integer, nullable=False)
    periodo_rotacion = db.Column(db.Integer, nullable=False)
    superficie_agua = db.Column(db.Integer, nullable=False)
    diametro = db.Column(db.Integer, nullable=False)

    def __init__(self, id, name, clima, poblacion, periodo_rotacion, superficie_agua, diametro):
        self.id = id
        self.name = name
        self.clima = clima
        self.poblacion = poblacion
        self.periodo_rotacion = periodo_rotacion
        self.superficie_agua = superficie_agua
        self.diametro = diametro

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "clima": self.clima,
            "poblacion": self.poblacion,
            "periodo_rotacion": self.periodo_rotacion,
            "superficie_agua": self.superficie_agua,
            "diametro": self.diametro,
        }
    
class Favorite(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(User)
    favorite_personaje = db.Column(db.Integer, db.ForeignKey("personaje.id"))
    personaje = db.relationship(Personaje)
    favorite_planeta = db.Column(db.Integer, db.ForeignKey("planeta.id"))
    planeta = db.relationship(Planeta)

    def __init__(self, id, user, favorite_personaje, favorite_planeta):
        self.id = id
        self.user = user
        self.favorite_personaje = favorite_personaje
        self.favorite_planeta = favorite_planeta

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "favorite_personaje": self.favorite_personaje,
            "favorite_planeta": self.favorite_planeta,
        }