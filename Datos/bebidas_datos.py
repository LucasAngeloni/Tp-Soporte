from sqlalchemy import exc,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Datos.bebida import Bebida,Base

class BebidaDatos(Bebida):

    def __init__(self):
        self.db = create_engine('mysql://root:lucas123@localhost:3306/vinos_mercado_libre')
        Base.metadata.bind = self.db
        db_session = sessionmaker()
        db_session.bind = self.db
        self.session = db_session()

    def get(self,codigo):

        try:
            bebida = self.session.query(Bebida).filter(Bebida.id_bebida == codigo).first()
        except exc.SQLAlchemyError:
            print("Error base de datos: ")
        else:
            return bebida

    def get_all(self):
        try:
            bebidas = self.session.query(Bebida).all()
        except exc.SQLAlchemyError:
            print("Error base de datos")
        else:
            return bebidas

    def get_all_tipo_bebida(self,tipo_bebida):
        try:
            bebidas = self.session.query(Bebida).filter(Bebida.tipo_bebida == tipo_bebida).all()
        except exc.SQLAlchemyError:
            print("Error base de datos")
        else:
            return bebidas

    def alta(self, bebida):
        try:
            self.session.add(bebida)
            self.session.commit()
        except exc.SQLAlchemyError:
            print('Error')
        else:
            print("Bebida dada de alta correctamente")

    def baja(self, cod):
        try:
            self.session.delete(self.session.query(Bebida).get(cod))
            self.session.commit()
        except exc.SQLAlchemyError as e:
            print("Error al dar de baja la bebida, "+e)
        else:
            print("Bebida dada de baja correctamente")

    def modificacion(self, bebida):
        try:
            x = self.session.query(Bebida).get(bebida.id_bebida)
            x.id_bebida = bebida.id_bebida
            x.titulo_bebida = bebida.titulo_bebida
            x.stock = bebida.stock
            x.precio = bebida.precio
            x.tipo = bebida.tipo
            self.session.commit()
        except:
            print("Error al modificar")
        else:
            print("Modficación completada")
