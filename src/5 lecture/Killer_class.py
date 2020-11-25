from fighters_main_class import Fighters
from Human_castes import Humans


class Killer(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 30
        damage_health = self.strenght*2
        self.print_for_special_ability_killer(enemy_fighter)
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_left_arm(self, enemy_fighter):
        self.up_point(1)
        self.health += 5
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*0.4
        self.print_for_attack_left_arm()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_killer(self, enemy_fighter):
        print(f'{self.name} простреливает колени сопернику {enemy_fighter.name}')
