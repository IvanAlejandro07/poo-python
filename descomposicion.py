
from typing_extensions import Self

''''' self es como un this en otros lenguajes
__init__ es como __contruct__ en php

'''

class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color

        # (_variable) es igual o parecido a private#
        self._estado = 'en_reposo'
        #none  = sin ningun valor#
        self._motor = Motor(cilindro=4)

    def acelerar (self, tipo = 'despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)


class Motor:

    def __init__(self, cilindro, tipo='gasolina'):
        self.cilindro = cilindro
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass



