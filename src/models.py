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
    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    favorite_personaje = db.Column(db.Integer, db.ForeignKey("personaje.id"))
    favorite_planeta = db.Column(db.Integer, db.ForeignKey("planeta.id"))

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












class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(42), unique=True, nullable=False)
    ki = db.Column(db.Integer, nullable=False)
    race = db.Column(db.String(48), nullable=False)

    def __init__(self, name, ki, race):
        self.name = name
        self.ki = ki
        self.race = race

    def serialize(self):
        return {
            "name": self.name,
            "ki": self.ki,
            "race": self.race,
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user = db.relationship("User")
    character_id = db.Column(db.Integer, db.ForeignKey('Character.id'), nullable=False)
    character = db.relationship("Character")

    def __init__(self, user, character):
        self.user = user
        self.character = character

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.serialize(),
            "character": self.character.serialize(),
        }