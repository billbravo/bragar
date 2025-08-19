from backend.producto import listar_productos
from backend.producto import consultar_producto
from backend.producto import crear_producto
from backend.producto import eliminar_producto
from backend.producto import actualizar_producto

print("Listar productos...")
productos = listar_productos()
print(productos)

print("Crear producto...")
producto_creado = crear_producto("9999", "iPhone 16", 600, 10)
print(f"Producto creado: {producto_creado}")

print("Consultar producto...")
producto = consultar_producto("9999")
print(producto)

print("Actualizar producto...")
producto_actualizado = actualizar_producto("9999", "iPhone 16 Pro", 900, 5)
print(f"Producto actualizado: {producto_actualizado}")
producto = consultar_producto("9999")
print(producto)

print("Eliminar producto...")
producto_eliminado = eliminar_producto("9999")
print(f"Producto eliminado: {producto_eliminado}")
productos = listar_productos()
print(productos)
