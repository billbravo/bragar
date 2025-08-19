from backend.hoja_producto import obtener_hoja_de_productos
from backend.excel import guardar_hoja

hoja = obtener_hoja_de_productos()

def listar_productos():
  filas = []
  ref_filas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
  
  for ref_fila in ref_filas:
    valores = []
    for celda in ref_fila:
      valores.append(celda.value)
    filas.append(valores)
    
  return filas

def consultar_producto(identificador):
  ref_filas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
  ref_filas_enum = enumerate(ref_filas)
  
  for idx, ref_fila in ref_filas_enum:
    if ref_fila[0].value == identificador:
      valores = []
      valores.append(idx)
      
      for celda in ref_fila:
        valores.append(celda.value)
        
      return valores
    
  else:
    return None

def crear_producto (identificador, nombre, precio, cantidad):
  if consultar_producto(identificador) != None:
    print(f"El producto con ID {identificador} ya existe.")
    return False
  
  producto= (identificador, nombre, precio, cantidad)
  hoja.append(producto)
  guardar_hoja(hoja)

  return True

def eliminar_producto(identificador):
  producto = consultar_producto(identificador)
  if producto == None:
    return False
  hoja.delete_rows(producto[0] + 2)
  guardar_hoja(hoja)

  return True

def actualizar_producto(identificador, nombre, precio, cantidad):
  producto = consultar_producto(identificador)
  if producto == None:
    return False
  hoja.delete_rows(producto[0] + 2)
  hoja.append((identificador, nombre, precio, cantidad))
  guardar_hoja(hoja)

  return True
  