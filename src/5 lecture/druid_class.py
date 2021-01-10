from fighters_main_class import Fighters
from mages_castes import Mages


class Druid(Mages):

    def _up_attributes_druid(self, value_strenght, value_defence, value_health):
        self.strenght += (value_strenght+(self.points*0.5))
        self.defence += value_defence
        self.health += (value_health+(self.points*1))

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self._up_attributes_druid(15, 8, 50)
        self.strenght += 15
        self.defence += 8
        self.health += 50
        self.print_for_special_ability(
            f'превратился в волка и сильно ранил {enemy_fighter.name}')
        enemy_fighter.take_damage(0, 0, 0, self.strenght*2)

    def attack_right_leg(self, enemy_fighter):
        self.up_point(4)
        self.print_for_attack_right_leg()
        enemy_fighter.take_damage(15, 0, 0, self.strenght*0.7)


druid = Druid('Друид', 260, 120, 95, 'Коготь зверя', 2850, 50)
