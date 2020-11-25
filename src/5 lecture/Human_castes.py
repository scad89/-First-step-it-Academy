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
        self.flag_up_armor = True
        self.flag_up_strengh = True

    def up_armor_human(self):
        if self.health < 300 and self.flag_up_armor == True:
            self.defence += self.armor
            self.flag_up_armor = False
            self.print_for_up_armor_human()

    def up_strenght(self):
        if self.health < 100 and self.flag_up_strengh == True:
            self.strenght += 80
            self.flag_up_strengh = False
            self.print_for_up_strenght()

    def attack_right_leg(self, enemy_fighter):
        self.up_point(5)
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*0.8
        self.print_for_attack_right_leg()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_up_armor_human(self):
        print(f'Броня {self.name} повышена на {self.points} очков')
        print()

    def print_for_up_strenght(self):
        print(f'Атака {self.name} увеличина на 80 единиц')
        print()
