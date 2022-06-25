
import getpass


class Persona():

    def __init__(self, nombre, contrasena):

        self.nombre = nombre
        self.contrasena = contrasena

    def login(self):

        _nombre = 'ivan'
        _contrasena = '123'

        if self.nombre == _nombre and self.contrasena == _contrasena:

            print('Ingresaste')
            print(('El nombre de la persona: '), self.nombre)
            print('La contraseña de la persona es', self.contrasena)
            
        else:
            print('Contraseña o Nombre incorrecto')


class Mostrar(Persona):

    def __init__(self, nombre, contrasena):
        super().__init__(nombre, contrasena)

    def login(self):
        return super().login()


if __name__ == '__main__':

    nombre = input('Introduce tu nombre: ')
    contrasena = getpass.getpass(prompt='Introduce tu contraseña')

    persona = Mostrar(nombre, contrasena)
    persona.login()
