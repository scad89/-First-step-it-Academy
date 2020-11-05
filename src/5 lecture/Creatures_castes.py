from fighters_main_class import Fighters


class Creatures(Fighters):
    def __init__(self, name, strenght, defence, energy, ammo, health, rage):
        self.name = name
        self.strenght = strenght
        self.defence = defence
        self.energy = energy
        self.ammo = ammo
        self.health = health
        self.points = 0
        self.rage = rage
        self.flag = True

    def use_rage(self):
        if self.health < 200 and self.flag == True:
            self.strenght += self.rage
            self.flag = False
            print(
                f'{self.name} использует "Ярость" для увеличения атаки')
            print()
