class Student:

    def __init__(self, nombre):
        self.nombre = nombre
        self.__notas = []
    
    def get_nota(self, indice):
        nota = self.__notas[indice]
        if nota > 11:
            return nota
        else:
            raise Exception("Usted no puede ver esta nota")

    def set_nota(self, nota):
        if len(self.__notas) >= 3:
            raise Exception("todas las notas ya han sido registradas")
        else:
            self.__notas.append(nota)

    @property
    def promedio(self):
        sum = 0.0
        cantidad = 0.0
        for nota in self.__notas:
            sum += nota
            cantidad += 1
        return sum / cantidad

studen1 = Student("Jaimito")
studen1.set_nota(10)
studen1.set_nota(15)
studen1.set_nota(8)

print(studen1.get_nota(1))

print(studen1.promedio)