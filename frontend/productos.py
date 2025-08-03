from utils.terminal import limpiar

def listarProductos ():
    print("Escogiste la opción de listar productos.")

def consultarProducto ():
    print("Escogiste la opción de consultar producto.")

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


