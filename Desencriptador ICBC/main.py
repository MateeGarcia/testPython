import xlrd
import xlsxwriter

#Entrada
oldPath = "C:\\Users\\ICBC\\Downloads\\EXCEL-ENCRIPTADO-Y-ORDENADO.xls"
openOldFile = xlrd.open_workbook(oldPath)
old_sheet = openOldFile.sheet_by_name("Sheet0")

#Salida
newPath = "C:\\Users\\ICBC\\Downloads\\Archivo-desencriptado.xls"
new_excel = xlsxwriter.Workbook(newPath)
new_sheet = new_excel.add_worksheet()

#Recorro el excel en la posición 1 que es la que tiene los nombres para desencriptar
for i in range(old_sheet.nrows):
    herramienta = old_sheet.cell_value(i,1)

#Transformo el nombre en una lista para poder recorrerlo letra por letra
    herramienta = list(herramienta)
    elementSize = len(herramienta)

#Recorro el nombre letra por letra
    for j in range(elementSize):
#Transformo la letra en una lista para poder compararla
        herramienta[j] = list(herramienta[j])
# Modifico las letras para desencriptar
        if herramienta[j] == ['A']:
            herramienta[j] = 'E'
        elif herramienta[j] == ['B']:
            herramienta[j] = 'V'
        elif herramienta[j] == ['C']:
            herramienta[j] = 'D'
        elif herramienta[j] == ['D']:
            herramienta[j] = 'C'
        elif herramienta[j] == ['E']:
            herramienta[j] = 'A'
        elif herramienta[j] == ['F']:
            herramienta[j] = 'H'
        elif herramienta[j] == ['G']:
            herramienta[j] = 'J'
        elif herramienta[j] == ['H']:
            herramienta[j] = 'F'
        elif herramienta[j] == ['I']:
            herramienta[j] = 'Y'
        elif herramienta[j] == ['J']:
            herramienta[j] = 'G'
        elif herramienta[j] == ['K']:
            herramienta[j] = 'Q'
        elif herramienta[j] == ['L']:
            herramienta[j] = 'R'
        elif herramienta[j] == ['M']:
            herramienta[j] = 'N'
        elif herramienta[j] == ['N']:
            herramienta[j] = 'M'
        elif herramienta[j] == ['O']:
            herramienta[j] = 'U'
        elif herramienta[j] == ['P']:
            herramienta[j] = 'T'
        elif herramienta[j] == ['Q']:
            herramienta[j] = 'K'
        elif herramienta[j] == ['R']:
            herramienta[j] = 'L'
        elif herramienta[j] == ['S']:
            herramienta[j] = 'Z'
        elif herramienta[j] == ['T']:
            herramienta[j] = 'P'
        elif herramienta[j] == ['U']:
            herramienta[j] = 'O'
        elif herramienta[j] == ['V']:
            herramienta[j] = 'B'
        elif herramienta[j] == ['W']:
            herramienta[j] = 'X'
        elif herramienta[j] == ['X']:
            herramienta[j] = 'W'
        elif herramienta[j] == ['Y']:
            herramienta[j] = 'I'
        elif herramienta[j] == ['Z']:
            herramienta[j] = 'S'
#Vuelvo a transformar la letra en un string
        herramienta[j] = "".join(herramienta[j])

#Transformo la lista de letras en un string (el nombre)
    herramienta = "".join(herramienta)
    new_sheet.write(i,0, herramienta)

#Cierro el nuevo excel
new_excel.close()