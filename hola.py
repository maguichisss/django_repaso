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

#import csv
#
#total = 0
#ventas_vendedores = {}
#with open('dashboard_ventas.csv') as f:
#    #lineas = [l for l in csv.DictReader(f)]
#    lineas = []
#    for row in csv.DictReader(f):
#        if row["CANTIDAD_VENDIDA"] == '':
#            continue
#        lineas.append(row)
#        total+=int(row["CANTIDAD_VENDIDA"])
#        if ventas_vendedores.get(row["VENDEDOR"]):
#            ventas_vendedores[row["VENDEDOR"]]+= int(row["CANTIDAD_VENDIDA"])
#        else:
#            ventas_vendedores[row["VENDEDOR"]] = int(row["CANTIDAD_VENDIDA"])
#
#print(ventas_vendedores)

#class Pokemon():
#    def __init__(self, nombre):
#        self.nombre = nombre
#    def mover(self):
#        print(f"{self.nombre} camina en 4 patas")
#    def comer(self):
#        print(f"{self.nombre} come")
#
#class Pikachu(Pokemon):
#    def mover(self):
#        print(f"{self.nombre} camina en 4 patas")
#class Onix(Pokemon):
#    def mover(self):
#        print(f"{self.nombre} se arrastra")
#
#
#
#
#pk1 = Pikachu("Pikachu")
##pk2 = Pokemon("Mew")
#pk3 = Onix("Onix")
#
#pk1.mover()
##pk2.mover()
#pk3.mover()



class Carro():
    def __init__(self, modelo, year, marca):
        self.llantas = 4
        self.modelo = modelo
        self.year = year
        self.marca = marca
    def acelerar(self):
        self.velocidad += 2
    def encender(self):
        self.distancia = 0
    def frenar(self):
        self.velocidad -= 1
    def apagar(self):
        self.velocidad = 0
    def __repr__(self):
        return f"{self.modelo} - {self.marca} - {self.year} - {self.llantas}\n"
class Lamborgini(Carro):
    def __init__(self, modelo, year):
        Carro.__init__(self, modelo, year, "Lamborgini")
    def avanzar(self):
        self.distancia += 5
    def reversa(self):
        self.distancia -= 4
class CarritoDeMulas(Carro):
    def avanzar(self):
        self.distancia += 1
    def reversa(self):
        self.distancia -= 1
    def turbo(self):
        self.distancia+=8
    def trampa(self, player):
        player.distancia -= 3
    def girar():
        self.vuelta_cerrada = 90

distancia_total = 10
lambo = Lamborgini("murcielago", 2013)
carMu = CarritoDeMulas("aventador de mulas", 1980, "patito")
lambo.encender()
carMu.encender()
ganador = False
while not ganador:
    if (lambo.distancia >= distancia_total) and (carMu.distancia >= distancia_total):
        ganador = "EMPATE"
    elif lambo.distancia >= distancia_total:
        ganador = lambo.modelo
    elif carMu.distancia >= distancia_total:
        ganador = carMu.modelo
    print(lambo.modelo, lambo.distancia)
    print(carMu.modelo, carMu.distancia)
    lambo.avanzar()
    carMu.avanzar()
    carMu.turbo()
    carMu.trampa(lambo)

print(f"El carro ganador es: {ganador}")
