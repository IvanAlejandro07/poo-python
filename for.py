'''''
def f(x):

    respuesta = 5

    for i in range(1000):
        respuesta += 1

    for i in range (x):
        respuesta += x

    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1

    return respuesta

print (f(5))
'''

def f(n):

    for i in range(n):

        for j in range(n):
            print(i, j)


print(5)



def fibonacci(n):

    if n == 0 or n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n -2)

print (fibonacci(8))



'''''Un loop => crecimiento lineal.
Un loop dentro de otro => crecimiento cuadratico
Llamadas recursivas => crecimiento exponecncial.'''