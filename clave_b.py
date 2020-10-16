import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""


# start-->
def suma(nummer1,nummer2,nummer3):
    suma = nummer1+nummer2+nummer3
    return suma


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""


# start-->
def sumaImpares():
    result = 0
    numero=1
    while numero<=1000:
        check = numero%2
        if check!=0:
            result +=numero
        numero+=1
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m

perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""


# start-->
def definicionEsfera(radio):
    perimetro = obtenerPerimetro(radio)
    area = obtenerArea(radio)
    volumen = obtenerVolumen(radio)
    result = {
    "perimetro": perimetro,
    "area": area,
    "volumen": volumen,
}
    return result


def obtenerPerimetro(radio):
    result = 2*math.pi*radio
    return result


def obtenerArea(radio):
    result = 4*math.pi*(radio**2)
    return result


def obtenerVolumen(radio):
    result = (4/3)*math.pi*(radio**3)
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Esfera:
    def __init__(self):
        pass

    def definicionEsfera(self,radio):
        self.radio=radio
        perimetro = obtenerPerimetro(self.radio)
        area = obtenerArea(self.radio)
        volumen = obtenerVolumen(self.radio)
        result = {
            "perimetro": perimetro,
            "area": area,
            "volumen": volumen,
        }
        return result

    def obtenerPerimetro(self):
        result = 2*math.pi*self.radio
        return result

    def obtenerArea(self):
        result = 4*math.pi*(self.radio**2)
        return result

    def obtenerVolumen(self):
        result = (4/3)*math.pi*(self.radio**3)
        return result


"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""


class Banco:
    def __init__(self):
        self.ListaClientes = []
        
    def procesar(self,cliente):
        self.ListaClientes.append(cliente)

    def abonosSanSalvador(self):
        i=0
        totalAbonosSS = 0
        while i<=(len(self.ListaClientes)-1):
            mytuple = self.ListaClientes[i]
            if mytuple[3]=="abono" and mytuple[1]=="san salvador":
                totalAbonosSS += mytuple[4]
            i+=1
        return float(totalAbonosSS)

    def abonosBalYRod(self):
        i=0
        totalBalYRod = 0
        while i<=(len(self.ListaClientes)-1):
            mytuple = self.ListaClientes[i]
            if mytuple[3]=="abono" and (mytuple[0]=="balbino" or mytuple[0]=="rodrigo"):
                totalBalYRod+=mytuple[4]
            i+=1
        return float(totalBalYRod)


class Cliente:
    def agregarCliente(self,nombre,lugar,numCuenta,transaccion,monto):
        Cliente = (nombre,lugar,numCuenta,transaccion,monto)
        return Cliente



"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/DAP-web/Examen-Parcial-QuiPython"
