from backend.excel import obtener_libro

libro = obtener_libro()
titulo_hoja = "clientes"


def inicializar_hoja():
  hoja = libro.reate_sheet(title=titulo_hoja)
  hoja.column_dimensions['A'].width = 25
  hoja.column_dimensions['B'].width = 15
  hoja.column_dimensions['C'].width = 15
  hoja.column_dimensions['D'].width = 15

  cabeceras = ("Número de documento", "Nombre", "Celular", "Ciudad")

  hoja.append(cabeceras)

  return hoja


def obtener_hoja_de_clientes():
  if titulo_hoja in libro.sheetnames:
    return libro[titulo_hoja]
  else:
    return inicializar_hoja() 
