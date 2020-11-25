from fighters_main_class import Fighters
from Human_castes import Humans


class Knight(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*2
        self.print_for_special_ability_knight(enemy_fighter)
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_headbutt(self, enemy_fighter):
        self.up_point(5)
        self.strenght += 5
        damage_defence = 10
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*0.8
        self.print_for_attack_headbutt()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_knight(self, enemy_fighter):
        print(f'{self.name} проткнул копьём {enemy_fighter.name}')
