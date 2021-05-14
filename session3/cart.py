class Product:
    precio = 0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Retornar objeto como texto
    def __str__(self):
        return f"{self.nombre} {self.precio}"
    # Retornar comparacion de objetos
    def __lt__(self, other):
        return self.precio < other.precio
    # Retorna una operacion de igualdad entre objetos
    def __eq__(self, other):
        return self.precio == other.precio

class Cart:
    products = []

    # Resuelve el operador de suma
    def __add__(self, other):
        self.products.append(other)

    def add_product(self, producto):
        self.products.append(producto)

    # Permite usar un metodo como un atributo
    @property
    def total(self):
        total = 0
        for producto in self.products:
            total += producto.precio
        return total 

iphone = Product("iphone12", precio=6000)
iphone_rojo = Product("iphone11", precio=6000)
macbook = Product(nombre="macbook", precio=8000)

cart = Cart()
cart + iphone
#cart.add_product(macbook)
#cart.add_product(iphone)

print(cart.products[0])
print(iphone < macbook)