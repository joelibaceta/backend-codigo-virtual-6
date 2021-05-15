from datetime import datetime

class Spy:

    nombre = "unkown"
    def __init__(self) -> None:
        self.ultima_modificacion = datetime.now()

    def __setattr__(self, att, val):
        super().__setattr__(self, 'ultima_modificacion', datetime.now())



espia = Spy()
print(espia.ultima_modificacion)
espia.nombre = "James Bond"
print(espia.ultima_modificacion)
