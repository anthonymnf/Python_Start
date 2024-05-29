import pandas as pd

data = pd.read_excel("data/VendaCarros.xlsx")

print(data.head())
print(data["Fabricante"].value_counts())
