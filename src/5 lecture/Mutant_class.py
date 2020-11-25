from fighters_main_class import Fighters
from Creatures_castes import Creatures


class Mutant(Creatures):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*2
        self.print_for_special_ability_mutant(enemy_fighter)
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_left_leg(self, enemy_fighter):
        self.up_point(3)
        self.health += 60
        self.strenght += 10
        damage_defence = 5
        damage_strenght = 3
        damage_energy = 0
        damage_health = self.strenght*0.5
        self.print_for_attack_left_leg()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_mutant(self, enemy_fighter):
        print(f'{self.name} проткнул {enemy_fighter.name} своими щупальцами')
