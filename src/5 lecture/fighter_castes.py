from fighters_main_class import Fighters


class Humans(Fighters):
    def __init__(self, name, strenght, defence, energy, ammo, health):
        self.name = name
        self.strenght = strenght
        self.defence = defence
        self.energy = energy
        self.ammo = ammo
        self.health = health
        self.points = 0
        self.armor = self.points
        self.flag = True

    def up_armor_human(self):
        if self.health < 300 and self.flag == True:
            self.defence += self.armor
            self.flag = False
            print(f'Броня {self.name} повышена на {self.points} очков')
            print()

    def up_strenght(self):
        if self.health < 100 and self.flag == True:
            self.strenght += 25
            self.flag = False
            print(f'Атака {self.name} увеличина на 25 единиц')
            print()


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
