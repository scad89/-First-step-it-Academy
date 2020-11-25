from fighters_main_class import Fighters
from Human_castes import Humans


class Soldier(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*2.5
        self.print_for_special_ability_soldier()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        damage_defence = 30
        damage_strenght = 5
        damage_energy = 10
        damage_health = self.strenght*1.5
        self.print_for_attack_ammo()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_soldier(self):
        print(f'{self.name} бросил гранату')
