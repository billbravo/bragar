from utils.terminal import limpiar
import backend.cliente as Cliente
from tabulate import tabulate

headers = ["ID","Nombre","Precio","Cantidad"]

def listarProductos ():
    print("Escogiste la opción de listar productos.")

    Clientes = Cliente.listar_clientes()
    print(tabulate(Clientes, headers=headers, tablefmt="rounded_grid"))

def consultarProducto ():
    
    ID = input("Ingrese el ID del producto que desea consultar: ")
    producto = Cliente.consultar_cliente(ID)

    if producto == None:
        print(f"Producto {ID} no encontrado.")
        return

    print(tabulate([producto[1:]], headers=headers, tablefmt="rounded_grid"))

def mostrarMenuProducto ():
    separador = "---------------------------------------"
    bienvenida = "USUARIO"
    opciones = {
        "1": listarProductos,
        "2": consultarProducto,
    }
    solicitud= "Ingrese una opción: "
    salida = False

    while True:
        menu = f"{bienvenida if salida == False else separador}\n1.Listar Productos\n2.Consultar Producto\n3.Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False

        if opcion == "3":
            limpiar()
            break

        if opcion in opciones:
            salida = True
            solicitud = "Ingrese una opción: "
            limpiar()
            opciones.get(opcion)()   

        else:   
            solicitud = "Opción no válida, intente de nuevo: "
            limpiar()


