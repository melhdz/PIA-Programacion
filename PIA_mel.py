#region Librerias
# Se importan las librerías que ocuparemos
import os
import csv
import re
#endregion

#region Definicion de clase
# Creamos la clase del cliente que se va a utilizar
class Cliente:
    def __init__(self, no_cliente, nombre, apellido, correo, no_compras):
        self.no_cliente = no_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.no_compras = no_compras
#endregion

#region Funciones y listas
# Creamos la lista que va a contener la información y las funciones Regex (Validaciones)
clientes = []
valid_letras = "^[a-zA-Z ]+$"
valid_correo = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
valid_num = "^[0-9]*$"

# Funcion para limpiar consola
Clear = lambda: os.system('cls')
#endregion

#region Procedimientos y Funciones
# Procedimiento para mostrar cuando exista un error
def error():
    print("Error: Ingresa un dato valido.")
    input("Presiona cualquier tecla para continuar.")

# Funcion booleana que valida si una variable coincide con la funcion Regex introducida
def RegEx(_txt,_regex):
    coincidencia = re.match(_regex, _txt)
    return bool(coincidencia)

# Función que te dice dónde se ubica el cliente que se busca
def noIndice(buscar):
    contador = -1
    indice_retorno = -1
    for posicion in clientes:
        contador = contador + 1
        if (posicion.no_cliente == buscar):
            indice_retorno = contador
            break
    return indice_retorno

# Función que te dice si el cliente existe en la lista
def BuscarCliente(no_cliente):
    coincidencia = False
    for cliente in clientes:
        if (cliente.no_cliente == no_cliente):
            coincidencia = True
            break
    return coincidencia

# Procedimiento para agregar un cliente nuevo
def agregarCliente():
    print("**Agregar Cliente**")
    while True:
        no_cliente = input("No. de Cliente: ")
        if re.match(valid_num,no_cliente):
            if no_cliente == "":
                    break

            if BuscarCliente(no_cliente):
                print("Error: Cliente ya existe!.")
                input("Presiona cualquier tecla para continuar.")
                break

            else:
                nombre = input("Nombre: ")

                if re.match(valid_letras,nombre):
                    apellido = input("Apellido: ")

                    if re.match(valid_letras, apellido):
                            correo = input("Correo electronico: ")

                            if re.match(valid_correo, correo):
                                no_compras = input("Número de compras: ")

                                if re.match(valid_num, no_compras):
                                    nuevo_cliente = Cliente(no_cliente, nombre, apellido, correo, no_compras)
                                    clientes.append(nuevo_cliente)
                                    print("Cliente registrado correctamente.")
                                    input("Presiona cualquier tecla para continuar.")
                                    break

                                else:
                                    error()
                                    break
                            else:
                                error()
                                break
                    else:
                        error()
                        break
                else:
                    error()
                    break
        else:
            error()
            break

# Procedimiento para buscar un cliente ya registrado
def buscarcliente():
    print("**Buscar cliente**")
    while True:
        no_cliente = input("No.Cliente a buscar: ")
        if no_cliente == "":
                break

        if re.match(valid_num,no_cliente):

            if BuscarCliente(no_cliente):
                posicion = noIndice(no_cliente)
                print("")
                print("**Datos del Cliente**")
                print("")
                print(f"No. cliente: {clientes[posicion].no_cliente}")
                print(f"Nombre: {clientes[posicion].nombre}")
                print(f"Apellido: {clientes[posicion].apellido}")
                print(f"Correo: {clientes[posicion].correo}")
                print(f"No. de compras: {clientes[posicion].no_compras}")
                input("Presiona cualquier tecla para continuar.")
                break

            else:
                print("Cliente no encontrado.")
                input("Presiona cualquier tecla para continuar.")
                break
        else:
            error()

# Procedimiento para modificar la información de un cliente
def modificarcliente():
    print("**Modificar cliente**")

    while True:
        no_cliente = input("No.Cliente a editar: ")
        if no_cliente == "":
                break

        if re.match(valid_num,no_cliente):
            if BuscarCliente(no_cliente):
                posicion = noIndice(no_cliente)
                print("")
                print("**Datos del cliente**")
                print("")
                print(f"No. cliente: {clientes[posicion].no_cliente}")
                print(f"Nombre: {clientes[posicion].nombre}")
                print(f"Apellido: {clientes[posicion].apellido}")
                print(f"Correo: {clientes[posicion].correo}")
                print(f"No. de compras: {clientes[posicion].no_compras}")

                while True:
                    print("**Nuevos datos**")
                    nombre = input("Nombre: ")

                    if re.match(valid_letras,nombre):
                        apellido = input("Apellido: ")

                        if re.match(valid_letras, apellido):
                                correo = input("Correo electronico: ")

                                if re.match(valid_correo, correo):
                                    no_compras = input("Número de compras: ")

                                    if re.match(valid_num, no_compras):
                                        clientes[posicion].no_cliente = no_cliente
                                        clientes[posicion].nombre = nombre
                                        clientes[posicion].correo = correo
                                        clientes[posicion].no_compras = no_compras
                                        print("Informacion actualizada con exito!")
                                        input("Presiona cualquier tecla para continuar.")
                                        break

                                    else:
                                        error()
                                        break
                                else:
                                    error()
                                    break
                        else:
                            error()
                            break
                    else:
                        error()
                        break

# Procedimiento para eliminar los datos de un cliente
def eliminarcliente():
    print("**Eliminar Cliente**")
    
    while True:
        no_cliente = input("No.Cliente a eliminar: ")
        if no_cliente == "":
                break

        if re.match(valid_num,no_cliente):
            if BuscarCliente(no_cliente):
                posicion = noIndice(no_cliente)
                print(f"No. cliente: {clientes[posicion].no_cliente}")
                print(f"Nombre: {clientes[posicion].nombre}")
                print(f"Apellido: {clientes[posicion].apellido}")
                print(f"Correo: {clientes[posicion].correo}")
                print(f"No. de compras: {clientes[posicion].no_compras}")

                print("¿Esta seguro que desea eliminar al cliente? [1 = Sí / 0 = No]: ")
                respuesta = input()
                if re.match(valid_num,respuesta):
                    if respuesta == "1":
                        clientes.pop(posicion)
                        print("Cliente eliminado correctamente")
                        input("Presiona cualquier tecla para continuar.")
                        break
                    else:
                        print("El cliente solicitado no fue eliminado.")
                        input("Presiona cualquier tecla para continuar.")
                    break
                else:
                    error()
            else:
                print("Ese cliente no está registrado en la lista")
                input("Presiona cualquier tecla para continuar.")
                break
        else:
            error()

# Procedimiento para ver la información de todos los clientes en la lista, utilizando un for
def verlistaclientes():
    for cliente in clientes:
        print("{:>10} {:>10} {:>10} {:>10} {:>10}".format(
        cliente.no_cliente, cliente.nombre, 
        cliente.apellido, cliente.correo, 
        cliente.no_compras))
    input("Presiona cualquier tecla para continuar.")
#endregion

#region Mantener archivos en CSV
# Procedimiento para grabar la información en un archivo csv
def guardarinformacion():
    destino = os.path.abspath(os.getcwd())
    actualizar = destino + "\\clientes.csv"
    if os.path.exists(actualizar):
        f = open(actualizar,"w+")
    else:
        f = open(actualizar,"w+")
        f.write("NO.CLIENTE|NOMBRE|APELLIDO|CORREO|NO.COMPRAS\n")

    for elemento in clientes:
        f.write(f'{elemento.no_cliente}|{elemento.nombre}|{elemento.apellido}|{elemento.correo}|{elemento.no_compras}\n')
    f.close()
    print("Informacion guardada.")
    input("Presiona cualquier tecla para continuar.")


# Cargar informacion guardada del archivo CSV y si no existe omitir.
try:
    with open('clientes.csv', newline='') as csv_doc:
        archivo_csv = csv.reader(csv_doc, delimiter='|')
        for propiedad in archivo_csv:
            clientes.append(Cliente
            (propiedad[0],
            propiedad[1],
            propiedad[2],
            propiedad[3],
            propiedad[4]))
except:
    pass
#endregion

#region Menú principal
ciclo = True
while ciclo:
    Clear()
    # Se pregunta la opción
    print("A. Agregar un nuevo cliente")
    print("B. Editar Cliente.")
    print("C. Eliminar Cliente.")
    print("D. Ver todos los Clientes.")
    print("E. Guardar Informacion. ")
    print("F. Salir.")
    opc = input("¿Qué deseas hacer?  > ")

    if RegEx(opc,"^[ABCDEFabcdef]{1}$"):
        # Si la validación es correcta se ejecuta el procedimiento correspondiente a la opción ingresada
        _opc = opc.upper()
        if _opc == "A":
            agregarCliente()
        if _opc == "B":
            modificarcliente()
        if _opc == "C":
            eliminarcliente()
        if _opc == "D":
            verlistaclientes()
        if _opc == "E":
            guardarinformacion()
        if _opc == "F":
            print("Saliendo...")
            ciclo = False

    else:
        print("Error. Ingrese una opcion valida del menu")
        input("Presiona cualquier tecla para continuar.")
#endregion

