#Abstraccion de datos private public#
class Lavadora:

#Pass es para cuando no hay un cuerpo en esa funcion#

    def __init__ (self):
        pass

        #metodo publico#
    def lavar(self, temperatura = 'caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
        
        #metodos privados#
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque de agua {temperatura}')

    # el guion bajo antes de la variable significa o equivale a private#
    #en este caso un metodo privado pero tambien se pueden variables#
    def _anadir_jabon(self):
        print('anadiendo jabon')
    
    def _lavar(self):
        print('lavando la ropa')
    
    def _centrifugar(self):
        print('Centrifugar la ropa')    



if __name__ == '__main__':
    
    lavadora = Lavadora() 

    lavadora.lavar()




'''''Funciones como objetos de primera clase

las funciones de primera clase son las funciones que ejecutan otra funcion como parametro

Ejemplo: 

def presentarse(nombre):
	return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
	return f"¡Hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante):
	return funcion_entrante("David")

la funcion principal va a ejecutar otra funcion para que jale el programa

Resultado: 

>>> consume_funciones(presentarse)
'Me llamo David'

>>> consume_funciones(estudiemos_juntos)
'¡Hey David, aprendamos Python!'

'''


'''''Funciones anidadas

las funciones anidadas son las que se crean dentro de otra funcion
Ejemplo: 

def funcion_mayor():
	print("Esta es una función mayor y su mensaje de salida.")

	def librerias():
		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

	def frameworks():
		print("Algunos frameworks de Python son: Django, Dash y Flask.")

	frameworks()
	librerias()


Resultado:
>>> funcion_mayor()
Esta es una función mayor y su mensaje de salida.
Algunos frameworks de Python son: Django, Dash y Flask.
Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.


las funciones que se encuentran adentro no se ejecutan hasta que llamen a la mayor
Scope el orden de ejecucion


'''






'''''Ejenplo de decorador

def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

def zumbido():
	print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido)



Resultado

>>> zumbido()
Este es el último mensaje...
Buzzzzzz
Este es el primer mensaje ;)


otra forma de que de este resultado es : 
@funcion_decoradora
def zumbido():
	print("Buzzzzzz")

Explicacion: en la funcion le pasan la funcion zumbido y dentro la funcion anidad mandan a llamar esa funcion.


esto se le llama como metaprogramacion





'''