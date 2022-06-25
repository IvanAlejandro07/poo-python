#polimorfismo#

#Herencia: es tal cual la funcion#
#polimorfismo: el como la herencia pero modificamos las cosas por ejemplo las funciones#

class Persona():

    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print('Ando caminando')



class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar(self):
        print('Ando moviendome en mi bicicleta')

def main():
    persona = Persona('daniel')
    persona.avanzar()

    ciclista = Ciclista('david')
    ciclista.avanzar()

if __name__ == '__main__':
    main()

