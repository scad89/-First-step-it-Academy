from fighters_main_class import Fighters
from Mages_castes import Mages


class Sorceress(Mages):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        damage_defence = 5
        damage_strenght = 5
        damage_energy = 15
        damage_health = self.strenght*2
        self.print_for_special_ability_necromancer_sorceress()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_knee_blow(self, enemy_fighter):
        self.up_point(8)
        self.energy += 5
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*0.9
        self.print_for_attack_knee_blow()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_necromancer_sorceress(self):
        print(f'{self.name} призывает ледяной шторм')
