import openpyxl
import os

archivo = "backend/datos.xlsx"

def obtener_libro():
  if os.path.exists(archivo):
    return openpyxl.load_workbook(archivo)
  else:
    openpyxl.load_workbook()


def guardar_hoja(hoja):
  libro = hoja.parent
  libro.save()
