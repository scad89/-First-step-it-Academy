from fighters_main_class import Fighters
from Mages_castes import Mages


class Druid(Mages):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.strenght += 15
        self.defence += 8
        self.health += 50
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*2
        self.print_for_special_ability_druid(enemy_fighter)
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_right_leg(self, enemy_fighter):
        self.up_point(4)
        damage_defence = 15
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*0.7
        self.print_for_attack_right_leg()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_druid(self, enemy_fighter):
        print(f'{self.name} превратился в волка и сильно ранил {enemy_fighter.name}')
