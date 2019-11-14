from Datos.bebidas_datos import BebidaDatos
from Datos.bebida import Bebida

class NegocioBebida(object):

    def __init__(self):
        self.bebidas = BebidaDatos()

    def get(self,cod):

        return self.bebidas.get(cod)

    def get_all(self):

        return self.bebidas.get_all()

    def get_all_tipo_bebida(self,tipo_bebida):

        return self.bebidas.get_all_tipo_bebida(tipo_bebida)

    def alta(self,bebida):

        self.bebidas.alta(bebida)

    def baja(self,cod):

        self.bebidas.baja(cod)

    def modificacion(self,bebida):

        self.bebidas.modificacion(bebida)


if __name__ == "__main__":
    v = NegocioBebida()

    #v.baja(3)
    vino = v.get_all_vinos()
    print(vino[0].imagen)
    #v.alta(Vino(titulo_vino='Rutini',cantidad=10,precio=900))

