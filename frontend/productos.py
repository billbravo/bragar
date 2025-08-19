from utils.terminal import limpiar
import backend.producto as backend
from tabulate import tabulate

headers = ["ID","Nombre","Precio","Cantidad"]


def solicitar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    identificador = input(f"Ingrese el ID del producto {nombre}: ")
    precio = input(f"Ingrese el precio del producto {nombre}: ")
    cantidad = input(f"Ingrese la cantidad del producto {nombre}: ")

    return(identificador, nombre, precio, cantidad)


def listar_productos ():
    print("Escogiste la opción de listar productos.")
    productos = backend.listar_productos()
    print(tabulate(productos, headers=headers, tablefmt="rounded_grid"))


def consultar_producto ():
    identificador = input("Ingrese el ID del producto que desea consultar: ")
    producto = backend.consultar_producto(identificador)

    if producto == None:
        print(f"Producto {identificador} no encontrado.")
        return

    print(tabulate([producto[1:]], headers=headers, tablefmt="rounded_grid"))


def agregar_producto():
    nuevo_producto = solicitar_producto()
    producto_creado = backend.crear_producto(*nuevo_producto)

    if producto_creado:
        print("Producto creado exitosamente.")
    else:
        print("Error al crear el producto. Verifique los datos e intente nuevamente.")


def eliminar_producto():
    identificador = input("Ingrese el ID del producto que desea eliminar: ")
    producto_eliminado = backend.eliminar_producto(identificador)

    if producto_eliminado:
        print(f"Producto {identificador} eliminado exitosamente.")
    else:
        print(f"Producto {identificador} no encontrado o no se pudo eliminar.")


def actualizar_producto():
    nuevo_producto = solicitar_producto()
    producto_actualizado = backend.actualizar_producto(*nuevo_producto)
    
    if producto_actualizado:
        print(f"Producto {nuevo_producto[0]} actualizado exitosamente.")
    else:
        print(f"Producto {nuevo_producto[0]} no encontrado o no se pudo actualizar.")


def mostrar_menu_productos():
    separador = "---------------------------------------"
    bienvenida = "USUARIO"
    opciones = {
        "1": listar_productos,
        "2": consultar_producto,
        "3": agregar_producto,
        "4": eliminar_producto,
        "5": actualizar_producto
    }
    solicitud= "Ingrese una opción: "
    salida = False

    while True:
        menu = f"{bienvenida if salida == False else separador}\n1.Listar Productos\n2.Consultar Producto\n3.Agregar Producto\n4.Eliminar Producto\n5.Actualizar Producto\n6.Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False

        if opcion == "6":
            limpiar()
            break

        if opcion in opciones:
            salida = True
            solicitud = "Ingrese una opción: "
            limpiar()
            opciones.get(opcion)()   

        else:   
            solicitud = "Opción no válida. Intente de nuevo: "
            limpiar()


