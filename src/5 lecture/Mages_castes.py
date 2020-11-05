from fighters_main_class import Fighters


class Mages(Fighters):
    def __init__(self, name, strenght, defence, energy, ammo, health, elixir):
        self.name = name
        self.strenght = strenght
        self.defence = defence
        self.energy = energy
        self.ammo = ammo
        self.health = health
        self.points = 0
        self.elixir = elixir
        self.flag = True

    def recovery(self):
        if self.energy < 10 and self.flag == True:
            self.energy += self.elixir
            self.flag = False
            print(f'{self.name} использовал(а) эликсир для восстановления')
            print()

    def ghoul(self):
        if self.health < 200:
            self.health += 10
            print(
                f'{self.name} использует вампиризм для восстановления очков здоровья')
            print()
