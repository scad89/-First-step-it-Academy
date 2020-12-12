class Fighters:
    def __init__(self, name, strenght, defence, energy, ammo, health):
        self.name = name
        self.strenght = strenght
        self.defence = defence
        self.energy = energy
        self.ammo = ammo
        self.health = health
        self.points = 0

    def up_point(self, count_points):
        self.points += count_points

    def _drop_energy(self, count):
        self.energy -= count
        if 35 < self.energy < 45:
            self.strenght -= (self.strenght*0.01)
            self.print_for_drop_energy_5()
        elif 20 < self.energy < 30:
            self.strenght -= (self.strenght*0.02)
            self.print_for_drop_energy_10()
        elif 0 < self.energy < 10:
            self.strenght -= (self.strenght*0.03)
            self.print_for_drop_energy_15()

    def attack_left_arm(self, enemy_fighter):
        self.up_point(1)
        self._drop_energy(1)
        self.print_for_attack_left_arm()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.3)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        self._drop_energy(2)
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.5)

    def attack_left_leg(self, enemy_fighter):
        self.up_point(3)
        self._drop_energy(3)
        self.print_for_attack_left_leg()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.4)

    def attack_right_leg(self, enemy_fighter):
        self.up_point(4)
        self._drop_energy(4)
        self.print_for_attack_right_leg()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.6)

    def attack_knee_blow(self, enemy_fighter):
        self.up_point(5)
        self._drop_energy(4)
        self.print_for_attack_knee_blow()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.9)

    def attack_headbutt(self, enemy_fighter):
        self.up_point(5)
        self._drop_energy(3)
        self.print_for_attack_headbutt()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.7)

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        self._drop_energy(10)
        self.print_for_attack_ammo()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*1.3)

    def print_for_drop_energy_5(self):
        print(f'У {self.name} атака снижена на 5%')

    def print_for_drop_energy_10(self):
        print(f'У {self.name} атака снижена на 10%')

    def print_for_drop_energy_15(self):
        print(f'У {self.name} атака снижена на 15%')

    def print_for_attack_left_arm(self):
        print(f'{self.name} нанёс/нанесла удар левой рукой')

    def print_for_attack_right_arm(self):
        print(f'{self.name} нанёс/нанесла удар правой рукой')

    def print_for_attack_left_leg(self):
        print(f'{self.name} нанёс/нанесла удар левой ногой')

    def print_for_attack_right_leg(self):
        print(f'{self.name} нанёс/нанесла удар правой ногой')

    def print_for_attack_knee_blow(self):
        print(f'{self.name} нанёс/нанесла удар коленом')

    def print_for_attack_headbutt(self):
        print(f'{self.name} нанёс/нанесла удар головой')

    def print_for_attack_ammo(self):
        print(f'{self.name} использовал/использовала своё оружие, {self.ammo}')

    def take_damage(self, damage_defence, damage_strenght, damage_energy, damage_health):
        self.defence = self.defence - damage_defence
        self.strenght = self.strenght - damage_strenght
        self.energy = self.energy - damage_energy
        self.health = self.health - (damage_health-(self.defence*0.2))
        self.print_for_take_damage()

    def print_for_take_damage(self):
        print(
            f'У {self.name} осталось {int(self.health)} очков жизни')
        print()
