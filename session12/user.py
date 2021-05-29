from sqlalchemy import Column, Integer, String

class User(db.Base):
    __tablename__ = 'user'

    idUser = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(String)
    telefono = Column(String)
    correo = Column(String)