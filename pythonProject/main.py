import xlrd

filePath = "C:\\Users\\mateo\\Downloads\\PARADESENCRIPTAR2.xls"

openFile = xlrd.open_workbook(filePath)

sheet = openFile.sheet_by_name("Sheet0")

for i in range(sheet.nrows):
        herramienta = sheet.cell_value(i, 1)
        herramienta = herramienta + "Mateo"
        print(herramienta)