from fighters_main_class import Fighters
from mages_castes import Mages


class Sorceress(Mages):
    def _up_attributes_sorceress(self, value_energy):
        self.energy += (value_energy+(self.elixir*0.15))

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.print_for_special_ability('призывает ледяной шторм')
        enemy_fighter.take_damage(15, 5, 15, self.strenght*2)

    def attack_knee_blow(self, enemy_fighter):
        self.up_point(8)
        self._up_attributes_sorceress(5)
        self.print_for_attack_knee_blow()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.9)


sorceress = Sorceress('Волшебница', 320, 50, 95, 'Посох', 3000, 50)
