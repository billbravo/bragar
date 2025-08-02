from backend.cliente import listar_clientes
from backend.cliente import consultar_cliente


print("Listar clientes...")
clientes = listar_clientes()
print(clientes)


print("Consultar clientes...")
cliente = consultar_cliente("1101")
print(cliente)
