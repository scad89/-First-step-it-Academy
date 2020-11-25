from fighters_main_class import Fighters
from Human_castes import Humans


class Ninja(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*2
        self.print_for_special_ability_ninja()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        self.health += 50
        damage_defence = 12
        damage_strenght = 3
        damage_energy = 8
        damage_health = self.strenght*1.4
        self.print_for_attack_ammo()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_ninja(self):
        print(
            f'{self.name} бросает дымовую гранату и наносит удар катаной в уязвимое место')
