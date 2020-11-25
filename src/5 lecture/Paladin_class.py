from fighters_main_class import Fighters
from Human_castes import Humans


class Paladin(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.strenght += 10
        self.defence += 20
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*2.5
        self.print_for_special_ability_paladin(enemy_fighter)
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        self.health += 50
        damage_defence = 13
        damage_strenght = 4
        damage_energy = 0
        damage_health = self.strenght*0.4
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_paladin(self, enemy_fighter):
        print(f'{self.name} вызвал ауру и нанёс урон {enemy_fighter.name}')
