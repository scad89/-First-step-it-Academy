from fighters_main_class import Fighters
from Human_castes import Humans


class Archer(Humans):

    def _up_energy_archer(self, value):
        self.energy += value

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.print_for_special_archer(enemy_fighter)
        enemy_fighter.take_damage(0, 0, 0, self.strenght*2.3)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        self._up_energy_archer(10)
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.7)

    def print_for_special_archer(self, enemy_fighter):
        print(
            f'{self.name} производит выстрел взрывающейся стрелой {enemy_fighter.name}')


archer = Archer('Лучница', 380, 40, 70, 'Лук', 2700)
