class Coordenada:
    def __init__(self, x, y):
        self.y = x
        self.x = y

    def distancia(self, otra_cordenada):
        x_diff = (self.x - otra_cordenada.x) **2
        y_diff = (self.y - otra_cordenada.y) **2

        return (x_diff + y_diff)**0.5


#para cuando lo ejecutemos en la consola#
if __name__ == '__main__':
    coor_1 = Coordenada(3, 30)
    coor_2 = Coordenada(4, 8)

   # print (coor_1.distancia(coor_2))#
    print(isinstance(coor_2, Coordenada))