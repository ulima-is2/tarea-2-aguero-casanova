import sys
import copy

class Entrada:
    def __init__(self, pelicula_id, funcion, codigo):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.codigo = codigo
        #self.cantidad = cantidad
        
    def __clone__(self):
        return copy.deepcopy(self)

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class CinePlaneta:
    def __init__(self):
        peliculaIT = Pelicula(1, 'IT')
        peliculaHF = Pelicula(2, 'La Hora Final')
        peliculaD = Pelicula(3, 'Desparecido')
        peliculaDeep = Pelicula(4, 'Deep El Pulpo')

        peliculaIT.funciones = ['19:00', '20.30', '22:00']
        peliculaHF.funciones = ['21:00']
        peliculaD.funciones = ['20:00', '23:00']
        peliculaDeep.funciones = ['16:00']

        self.lista_peliculas = [peliculaIT, peliculaHF, peliculaD, peliculaDeep]
        self.entradas = []

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        entrada1 = Entrada(id_pelicula_elegida,funcion_elegida,1)
        entradas = []
        self.entradas.append(entrada1)
        print('xxx')
        for i in range(2, int(cantidad)+1, 1):
            entrada_copia = entrada1.__clone__()
            entrada_copia.codigo = i
            self.entradas.append(entrada_copia)

        return len(self.entradas)



class CineStark:
    def __init__(self):
        peliculaD = Pelicula(1, 'Desparecido')
        peliculaDeep = Pelicula(2, 'Deep El Pulpo')

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []


    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        entrada1 = Entrada(id_pelicula_elegida,funcion_elegida,1)
        entradas = []
        self.entradas.append(entrada1)
        print('xxx')
        for i in range(2, int(cantidad)+1, 1):
            entrada_copia = entrada1.__clone__()
            entrada_copia.codigo = i
            self.entradas.append(entrada_copia)

        return len(self.entradas)

def main():

    terminado = False

    while not terminado:

        cliente = principal()
        cine = cliente.elegir_cine()
        pelicula = cliente.elegir_pelicula(cine)
        funcion = cliente.elegir_funcion(cine, pelicula)
        cantidad_entradas = cliente.cantidad_entradas()
        codigo_entrada = cine.guardar_entrada(pelicula, funcion, cantidad_entradas)

        print(codigo_entrada)

        continuar = input("continuar?")
        if continuar == 'no':
            terminado = True

class principal():
    def elegir_cine(self):
        print('********************')
        print('Lista de cines')
        print('1: CinePlaneta')
        print('2: CineStark')
        print('********************')
        opcion = input("cine a elegir: ")
        
        if opcion == '1':
            # CinePlaneta
            cine = CinePlaneta()
        elif opcion == '2':
            cine = CineStark()
        return cine
    
    def elegir_pelicula(self, cine):
        peliculas = cine.listar_peliculas()
        print('********************')
        for pelicula in peliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        print('********************')
        pelicula = input('Elija pelicula:')
        return pelicula

    def elegir_funcion(self, cine, pelicula):
        print('Ahora elija la función (debe ingresar el formato hh:mm): ')
        for funcion in cine.listar_funciones(pelicula):
            print('Función: {}'.format(funcion))
        funcion = input('Funcion:')
        return funcion

    def cantidad_entradas(self):
        cantidad_entradas = input('Ingrese cantidad de entradas: ')
        return cantidad_entradas

    

if __name__ == '__main__':
    main()
