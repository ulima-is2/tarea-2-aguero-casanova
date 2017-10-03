import sys
import copy
import sqlite3
conn = sqlite3.connect(':memory:')

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


        return self.entradas



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

        return self.entradas

def main():

    #se debe crear la BD
    gestionar_BD = GestionDB()
    gestionar_BD.crearDB()

    terminado = False

    while not terminado:

        cliente = principal()
        cine = cliente.elegir_cine()
        pelicula = cliente.elegir_pelicula(cine)
        funcion = cliente.elegir_funcion(cine, pelicula)
        cantidad_entradas = cliente.cantidad_entradas()
        codigo_entrada = cine.guardar_entrada(pelicula, funcion, cantidad_entradas)

        print(len(entradas))

        #se envian las entradas para guardar
        gestionar_BD.guardar_entrada(entradas)


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


class GestionDB:

    def crearDB(self):

        c = conn.cursor()

        c.execute('''CREATE TABLE CINE
                         (id_cine INTEGER PRIMARY KEY, nombre_cine text )''')

        c.execute("INSERT into CINE values (1,'CinePlaneta')")
        c.execute("INSERT into CINE values (2,'CineStark')")

        c.execute('''CREATE TABLE PELICULA
                         (id_pelicula INTEGER PRIMARY KEY, nombre_pelicula text )''')

        #nuevo
        c.execute("INSERT into PELICULA values (1,'IT')")
        c.execute("INSERT into PELICULA values (2,'La Hora Final')")
        c.execute("INSERT into PELICULA values (3,'Desparecido')")
        c.execute("INSERT into PELICULA values (4,'Deep El Pulpo')")
        # hasta aca

        c.execute('''CREATE TABLE FUNCION
                        (id_funcion INTEGER PRIMARY KEY, hora_minuto TIMESTAMP)''')

        #nuevo funcion cine planeta
        c.execute("INSERT into FUNCION values (1,'19:00')")
        c.execute("INSERT into FUNCION values (2,'20:30')")
        c.execute("INSERT into FUNCION values (3,'22:00')")
        c.execute("INSERT into FUNCION values (4,'21:00')")
        c.execute("INSERT into FUNCION values (5,'20:00')")
        c.execute("INSERT into FUNCION values (6,'23:00')")
        c.execute("INSERT into FUNCION values (7,'16:00')")
        #nuevo funcion cine stark
        c.execute("INSERT into FUNCION values (8,'21:00')")
        c.execute("INSERT into FUNCION values (9,'23:00')")
        c.execute("INSERT into FUNCION values (10,'16:00')")
        c.execute("INSERT into FUNCION values (11,'20:00')")


        

        c.execute('''CREATE TABLE CINE_PELICULA
                        (id_cine INTEGER, id_pelicula INTEGER,
                        PRIMARY KEY (id_cine, id_pelicula),
                        FOREIGN KEY(id_pelicula) REFERENCES PELICULA(id_pelicula)
                        )''')
          #Planeta
        c.execute("INSERT into CINE_PELICULA values (1,1)")
        c.execute("INSERT into CINE_PELICULA values (1,2)")
        c.execute("INSERT into CINE_PELICULA values (1,3)")
        c.execute("INSERT into CINE_PELICULA values (1,4)")
         #Stark
        c.execute("INSERT into CINE_PELICULA values (2,3)")
        c.execute("INSERT into CINE_PELICULA values (2,4)")

        c.execute('''CREATE TABLE PELICULA_FUNCION
                        (id_pelicula INTEGER, id_funcion INTEGER,
                        PRIMARY KEY (id_pelicula, id_funcion),
                        FOREIGN KEY(id_pelicula) REFERENCES PELICULA(id_pelicula),
                        FOREIGN KEY(id_funcion) REFERENCES FUNCION(id_funcion)
                        )''')

        c.execute("INSERT into PELICULA_FUNCION values (1,1)")
        c.execute("INSERT into PELICULA_FUNCION values (1,2)")
        c.execute("INSERT into PELICULA_FUNCION values (1,3)")
        c.execute("INSERT into PELICULA_FUNCION values (2,4)")
        c.execute("INSERT into PELICULA_FUNCION values (3,5)")
        c.execute("INSERT into PELICULA_FUNCION values (3,6)")
        c.execute("INSERT into PELICULA_FUNCION values (3,8)")
        c.execute("INSERT into PELICULA_FUNCION values (3,9)")
        c.execute("INSERT into PELICULA_FUNCION values (4,7)")
        c.execute("INSERT into PELICULA_FUNCION values (4,10)")
        c.execute("INSERT into PELICULA_FUNCION values (4,11)")




        conn.commit()
        c.close()
    def guardar_entrada(self)
        c = conn.cursor()

        #FALTA INSERTAR LAS ENTRADAS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! RIP

        c.execute("INSERT into ENTRADA values (1,'CinePlaneta')")
        c.execute('''CREATE TABLE ENTRADA
            (id_entrada INTEGER PRIMARY KEY, id_pelicula INTEGER, id_funcion INTEGER, cantidad INTEGER,
            FOREIGN KEY(id_pelicula) REFERENCES PELICULA(id_pelicula),
            FOREIGN KEY(id_funcion) REFERENCES FUNCION(id_funcion)
            )''')
        conn.commit()
        c.close()


if __name__ == '__main__':
    main()
