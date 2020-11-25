from fighters_main_class import Fighters
from Mages_castes import Mages


class Аrchmage(Mages):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.health += 100
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*2
        self.print_for_special_ability_archmage()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_archmage(self):
        print(f'{self.name} вызвал огненный дождь.')

    def attack_headbutt(self, enemy_fighter):
        self.up_point(5)
        damage_defence = 3
        damage_strenght = 3
        damage_energy = 3
        damage_health = self.strenght*0.7
        self.print_for_attack_headbutt()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)
