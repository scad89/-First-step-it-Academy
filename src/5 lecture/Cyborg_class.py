from fighters_main_class import Fighters
from Creatures_castes import Creatures


class Cyborg(Creatures):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.energy += 15
        self.defence += 100
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = 0
        self.print_for_special_ability_cyborg()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_knee_blow(self, enemy_fighter):
        self.up_point(5)
        self.health += 40
        damage_defence = 25
        damage_strenght = 5
        damage_energy = 6
        damage_health = self.strenght*0.85
        self.print_for_attack_knee_blow()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_cyborg(self):
        print(f'{self.name} использовал наноброню')
