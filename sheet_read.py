from openpyxl import load_workbook

# Lendo pasta de trabalho da planilha
wb = load_workbook("data/pivot_table.xlsx")
sheet = wb["Relatorio"]

# Acessando valor específico
# print(sheet["A3"].value)
# Funciona assim: print(sheet["Celula da planilha"].value)

for i in range(2, 6):
  ano= sheet["A%s" %i].value
  am = sheet["B%s" %i].value
  bt = sheet["C%s" %i].value
  print("Em {0} o Aston vendeu {1} e o Bentley vendeu {1}".format(ano, am, bt))
  