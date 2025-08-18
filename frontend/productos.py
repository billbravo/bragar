from utils.terminal import limpiar
import backend.cliente as Cliente
from tabulate import tabulate

headers = ["ID","Nombre","Precio","Cantidad"]

def solicitarProducto():
    nombre = input("Ingrese el nombre del producto: ")
    documento = input(f"Ingrese el ID del producto {nombre}: ")
    celular = input(f"Ingrese el precio del producto {nombre}: ")
    ciudad = input(f"Ingrese la cantidad del producto {nombre}: ")

    return(documento, nombre, celular, ciudad)

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

def agregarProducto():
    nuevo_producto = solicitarProducto()
    producto_creado = Cliente.crearProducto(*nuevo_producto)

    if producto_creado:
        print("Producto creado exitosamente.")
    else:
        print("Error al crear el producto. Verifique los datos e intente nuevamente.")

def eliminarProducto():
    documento = input("Ingrese el ID del producto que desea eliminar: ")
    producto_eliminado = Cliente.eliminarProducto(documento)

    if producto_eliminado:
        print(f"Producto {documento} eliminado exitosamente.")
    else:
        print(f"Producto {documento} no encontrado o no se pudo eliminar.")

def mostrarMenuProducto ():
    separador = "---------------------------------------"
    bienvenida = "USUARIO"
    opciones = {
        "1": listarProductos,
        "2": consultarProducto,
        "3": agregarProducto,
        "4": eliminarProducto
    }
    solicitud= "Ingrese una opción: "
    salida = False

    while True:
        menu = f"{bienvenida if salida == False else separador}\n1.Listar Productos\n2.Consultar Producto\n3.Agregar Producto\n4.Eliminar Producto\n5.Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False

        if opcion == "5":
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


