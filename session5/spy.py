from datetime import datetime

class Spy:

    nombre = "unkown"
    def __init__(self) -> None:
        self.ultima_modificacion = datetime.now()

    def __setattr__(self, att, val):
        super().__setattr__('ultima_modificacion', datetime.now())
        super().__setattr__(att, val)



espia = Spy()
print(espia.ultima_modificacion)
espia.nombre = "James Bond"
print(espia.ultima_modificacion)
print(espia.nombre)
