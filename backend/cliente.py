from backend.hoja_cliente import obtener_hoja_de_clientes

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
