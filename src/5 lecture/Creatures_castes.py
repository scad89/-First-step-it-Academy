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
        self.flag_use_rage = True

    def attack_left_arm(self, enemy_fighter):
        self.up_point(6)
        damage_defence = 5
        damage_strenght = 0
        damage_energy = 2
        damage_health = self.strenght*0.4
        self.print_for_attack_left_arm()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(7)
        damage_defence = 6
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*0.6
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def use_rage(self):
        if self.health < 400 and self.flag_use_rage == True:
            self.strenght += self.rage
            self.flag_use_rage = False
            self.print_for_use_rage()

    def print_for_use_rage(self):
        print(
            f'{self.name} использует "Ярость" для увеличения атаки')
        print()
