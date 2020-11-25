from fighters_main_class import Fighters
from Human_castes import Humans


class Archer(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*2.1
        self.print_for_special_archer(enemy_fighter)
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        self.energy += 10
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*0.7
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_archer(self, enemy_fighter):
        print(
            f'{self.name} производит выстрел взрывающейся стрелой {enemy_fighter.name}')
