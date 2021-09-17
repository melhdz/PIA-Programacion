#Traemos los módulos que se utilizan
import csv
import os
import re

#Se define la clase junto con sus atributos
class gym:
    estatus = "Activo"
    def __init__(self, clave, nombre, apellido_p, apellido_m, edad):
        self.clave = clave
        self.nombre = nombre
        self.apellido_p = apellido_p
        self.apellido_m = apellido_m
        self.edad = edad

#Se define la lista que contendrá las instancias de las clases
lista_clientes = []

#Región de expresiones regulares
rletras = "^[a-zA-Z ]+$"
rnumeros = "^[0-9]*$"
cargar = True

def Posicion(buscar):
    contador = -1
    posicion_numero = -1
    for posicion in lista_clientes:
        contador = contador + 1
        if (posicion.clave == buscar):
            posicion_numero = contador
            break
    return posicion_numero

# Función que te dice si el cliente existe en la lista
def BusquedaEspecifica(clave):
    encontrado = False
    for cliente in lista_clientes:
        if (cliente.clave == clave):
            encontrado = True
            break
    return encontrado


#Se define el menú principal que se mostrará al usuario
try:
    with open('clientes_gym.csv', newline='') as archivo:
        _archivo = csv.reader(archivo, delimiter='|')
        for i in _archivo:
            lista_clientes.append(gym(i[0],i[1],i[2],i[3],i[4]))
except:
    pass
while True:
    print("1. Registrar cliente.")
    print("2. Eliminar cliente.")
    print("3. Ver lista de clientes.")
    print("4. Guardar información al CSV.")
    print("0. Salir del sistema.")

    #Se le pregunta al usuario qué opcion desea realizar y se valida con regex que se ingrese un número del 0 al 6
    respuesta = input("Ingresa una opción: ")
    if re.match("^[0123456]{1}$", respuesta):
        if respuesta == "0":
            print("Saldras del sistema ")
            #Termina el programa si se indica la opción 0.
            break
        elif respuesta == "1":
            #Código para registrar un nuevo cliente al registro
            print("*****Registrar cliente*****")
            #Se define un ciclo infinito para preguntar los datos
            while True:
                clave = input("Ingrese la clave del cliente a registrar: ")
                if clave == "":
                        break
                else:
                    nombre = input("Ingrese el/los nombre(s) del cliente: ")
                    if re.match(rletras, nombre):
                        apellido_p = input("Ingrese el apellido paterno del cliente: ")
                        if re.match(rletras, apellido_p):
                            apellido_m = input("Ingrese el apellido materno del cliente: ")
                            if re.match(rletras, apellido_m):
                                try:
                                    edad = int(input("Ingrese su edad: "))
                                except:
                                    print("No se guardó el dato ")
                                    break
                                if edad >= 18 and edad <= 100:
                                        #Se instancia la clase con los datos que se dieron.
                                        cliente_nuevo = gym(clave, nombre, apellido_p, apellido_m, edad)
                                        lista_clientes.append(cliente_nuevo)
                                        print("El cliente se ha dado de alta. ")
                                        break
                                else:
                                    print("No se guardó el dato ")
                            else:
                                print("No se guardó el dato ")
                        else:
                            print("No se guardó el dato ")
                    else:
                        print("No se guardó el dato ")

        elif respuesta == "2":
            #Se elimina el cliente que el usuario indique con la clave que se desee buscar en el registro
            print("*****Borrar cliente*****")
            while True:
                clave = input("Ingrese la clave del cliente que desea eliminar: ")
                if clave == "":
                        break
                if re.match(rnumeros, clave):
                    if BusquedaEspecifica(clave):
                        posicion = Posicion(clave)
                        #Se imprimen los datos
                        print("\n*****Información del cliente*****")
                        print("\nClave: ",lista_clientes[posicion].clave)
                        print(f"Nombre: {lista_clientes[posicion].nombre} {lista_clientes[posicion].apellido_p} {lista_clientes[posicion].apellido_m}")
                        print("Edad: ",lista_clientes[posicion].edad)
                        respuesta = input("¿Desea eliminar el cliente del registro? [S/N]: ")
                        if respuesta.upper() == "S":
                            #Se elimina el cliente con pop tomando en cuenta la posición que regresa la función "indice"
                            lista_clientes.pop(posicion)
                            print("Cliente eliminado ")
                        else:
                            print("Cliente no eliminado. ")
                        break
                    else:
                        print("El cliente buscado no ha sido registrado ")
                        break
                else:
                    print("El dato no se ha guardado ")

        elif respuesta == "3":
            #Por cada registro de cliente en la lista "clientes" se imprimen los datos de cada uno.
            for cliente in lista_clientes:
                print(f"Clave: {cliente.clave}")
                print(f"Nombre Completo: {cliente.nombre} {cliente.apellido_p} {cliente.apellido_m}")
                print(f"Edad: {cliente.edad}")
                print()

        elif respuesta == "4":
            #Los datos se guardan en un archivo csv que se genera en la carpeta de trabajo actual.
            ruta = os.path.abspath(os.getcwd())
            archivo_trabajo = ruta + "\\clientes_gym.csv"
            f = open(archivo_trabajo,"w+")
            f.write("CLAVE|NOMBRE[S]|APELLIDO PATERNO|APELLIDO MATERNO|EDAD\n")
            for cliente in lista_clientes:
                f.write(f'{cliente.clave}|{cliente.nombre}|{cliente.apellido_p}|{cliente.apellido_m}|{cliente.edad}\n')

            f.close()
            print("El CSV ha sido refrescado. ")
    else:
        print("Opción elegida no encontrada.")