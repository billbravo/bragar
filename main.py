from backend.cliente import listar_clientes
from frontend.productos import mostrarMenuProducto

clientes = listar_clientes()

print(clientes)

mostrarMenuProducto()
