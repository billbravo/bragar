from backend.hoja_cliente import obtener_hoja_de_clientes
from backend.excel import guardar_hoja

hoja = obtener_hoja_de_clientes()

def listar_clientes():
  filas = []
  ref_filas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
  
  for ref_fila in ref_filas:
    valores = []
    for celda in ref_fila:
      valores.append(celda.value)
    filas.append(valores)
    
  return filas

def consultar_cliente(documento):


  ref_filas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
  ref_filas_enum = enumerate(ref_filas)
  
  for idx, ref_fila in ref_filas_enum:
    if ref_fila[0].value == documento:
      valores = []
      valores.append(idx)
      
      for celda in ref_fila:
        valores.append(celda.value)
        
      return valores
    
  else:
    return None

def crearProducto (documento, Nombre,Celular,Ciudad):
  if consultar_cliente(documento) != None:
    print(f"El producto con ID {documento} ya existe.")
    return False
  
  cliente= (documento, Nombre,Celular,Ciudad)

  hoja.append(cliente)

  guardar_hoja(hoja)

def eliminarProducto(documento):
  cliente = consultar_cliente(documento)
  if cliente == None:
    return False
  hoja.delete_rows(cliente[0] + 2)
  guardar_hoja(hoja)

  return True