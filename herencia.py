#Herencia#

##super clase
class Rectangulo:

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura

    def area(self):

        return self.base * self.altura


'''''Para la herencia en python se hace creando la clase
y en los parentesis llamar la clase de la cual es la 
herencia     en otros lenguajes es extends php y java'''


# super permite obtener un refencia directa de la super clase#
#podemos llamar el constructor de la super clase#


#subclase#
class Cuadrado(Rectangulo):
    def __init__(self,lado):
        super().__init__(lado, lado)





#estoy heredando el metodo area de la super clase rectangulo a la subclase cuadrado#
if __name__ == '__main__':

    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())