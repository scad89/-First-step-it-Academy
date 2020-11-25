from fighters_main_class import Fighters
from Human_castes import Humans


class Monk(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.strenght += 10
        self.defence += 10
        self.health += 100
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = 0
        self.print_for_special_ability_monk()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_left_arm(self, enemy_fighter):
        self.up_point(1)
        self.energy += 3
        damage_defence = 5
        damage_strenght = 0
        damage_energy = 1
        damage_health = self.strenght*0.4
        self.print_for_attack_left_arm()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        self.energy += 5
        damage_defence = 7
        damage_strenght = 0
        damage_energy = 2
        damage_health = self.strenght*0.6
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_monk(self):
        print(f'{self.name} прочитал молитву и увеличил свои атрибуты')
