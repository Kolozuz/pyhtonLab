import csv
 
# Cargar el archivo
myFile = open("DataAnalisis/data/notasxestudiante.csv", "r")
reader = csv.DictReader(myFile)
#Crea una lista de diccionarios
dataset = list(reader)

print(f"{dataset[1]}")
