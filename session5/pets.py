
class Pet:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def alimentar(self):
        print("alimentacion generica")

class Dog(Pet):
    def alimentar(self):
        print("dar croquetas")

class Cat(Pet):
    def alimentar(self):
        print("dar enlatado")

class Turtle(Pet):
    pass

mascotas = [
    Dog(nombre="firulais"),
    Cat(nombre="pelusa"),
    Turtle(nombre="veloz")
]

for mascota in mascotas:
    mascota.alimentar()