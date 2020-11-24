class Pokemon:
    def __init__(self, health, power, name):

        self.power = power
        self.health = health
        self.name = name


def showStats(first, second):
    print(f"""
---------------------------------------
{ first.name }
Vida { first.health }
Poder { first.power }
---------------------------------------
{ second.name }
Vida { second.health }
Poder { second.power }
---------------------------------------""")


def attack(first, second):
    first.health -= second.power
