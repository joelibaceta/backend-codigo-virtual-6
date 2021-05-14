class Empleado:

    numero_ventas = 0

    def __init__(self, nombre, apellido, salario, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.dni = dni

    def vender(self):
        self.numero_ventas += 1
        print("yey, hice una venta")

    def reportar(self):
        print(f"{self.nombre} vendio: {self.numero_ventas}")

juan = Empleado("juan", "perez", 3000, "12341234")
jhon = Empleado("jhon", "gutierrez", 2000, "24562345")
juan.salario = 4000
print(juan.salario)
juan.vender()
juan.reportar()
jhon.reportar()
