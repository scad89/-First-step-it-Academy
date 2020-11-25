from fighters_main_class import Fighters
from Human_castes import Humans


class Berserker(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 20
        damage_health = self.strenght*2
        self.print_for_special_ability_berserker(enemy_fighter)
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        self.strenght += 15
        self.energy += 10
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*1.7
        self.print_for_attack_ammo()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_berserker(self, enemy_fighter):
        print(
            f'{self.name} наносит удар топором {enemy_fighter.name}')
