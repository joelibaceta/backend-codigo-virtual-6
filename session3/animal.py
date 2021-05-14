class Mamal:

    def swim(self):
        print("swiming as a mamal...")

class Fish:

    def swim(self):
        print("swiming...")

class Dolphin(Mamal, Fish):
    pass

class Monkey(Mamal):
    pass

chita = Monkey()
flipper = Dolphin()

chita.swim()
flipper.swim()