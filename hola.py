#print("Cuantas materias tienes: ")
#numero_materias = int(input())
#calificaciones = []
#total = 0
#for mat in range(numero_materias):
#   print("Dame una calificacion: ")
#   cal = float(input())
#   calificaciones.append(cal)
#   total = total + cal
#promedio = sum(calificaciones)/len(calificaciones)
#print("FIN", total, promedio)
#if promedio >= 6:
#   print("APROBADO")
#else:
#   print("REPROBADO")
#diccionario = {
#   "ricardo": [12.0],
#   "haran": "25",
#   "paco": {
#       'paquito': 'pachangas',
#       'lalal': 12312,
#   },
#}
#print(diccionario)
#diccionario["mau"] = "algo"
#print(diccionario)
#

import csv

total = 0
ventas_vendedores = {}
with open('dashboard_ventas.csv') as f:
    #lineas = [l for l in csv.DictReader(f)]
    lineas = []
    for row in csv.DictReader(f):
        if row["CANTIDAD_VENDIDA"] == '':
            continue
        lineas.append(row)
        total+=int(row["CANTIDAD_VENDIDA"])
        if ventas_vendedores.get(row["VENDEDOR"]):
            ventas_vendedores[row["VENDEDOR"]]+= int(row["CANTIDAD_VENDIDA"])
        else:
            ventas_vendedores[row["VENDEDOR"]] = int(row["CANTIDAD_VENDIDA"])

print(ventas_vendedores)
