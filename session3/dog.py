class Animal:
    nombre = "animal"
    def __init__(self, nombre):
        self.nombre = nombre

    def dormir(self):
        print("zZzZ")

class Dog(Animal):

    def ladrar(self):
        print("woof")

class Cat(Animal):

    def maullar(self):
        print("meaw")

fido = Dog("Fido")
print(fido.nombre)
fido.ladrar()
fido.dormir()

pelusa = Cat("Pelusa")
print(pelusa.nombre)
pelusa.maullar()
pelusa.dormir()