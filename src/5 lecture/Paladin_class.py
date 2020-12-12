from fighters_main_class import Fighters
from Human_castes import Humans


class Paladin(Humans):
    def _up_attributes_paladin(self, value_strenght, value_defence, value_health):
        self.strenght += (value_strenght+self.energy*0.2)
        self.defence += value_defence
        self.health += (value_health+self.energy*0.3)

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self._up_attributes_paladin(10, 20, 0)
        self.print_for_special_ability_paladin(enemy_fighter)
        enemy_fighter.take_damage(0, 0, 0, self.strenght*2.5)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        self._up_attributes_paladin(0, 0, 20)
        self.health += 50
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(13, 4, 0, self.strenght*0.4)

    def print_for_special_ability_paladin(self, enemy_fighter):
        print(f'{self.name} вызвал ауру и нанёс урон {enemy_fighter.name}')


paladin = Paladin('Паладин', 300, 130, 70, 'Святой посох', 3300)
