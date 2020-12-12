from fighters_main_class import Fighters
from Mages_castes import Mages


class Prophet(Mages):
    def _up_attributes_prophet(self, value_strenght, value_energy, value_health):
        self.strenght += (value_strenght+self.elixir*0.05)
        self.energy += value_energy
        self.health += (value_health+self.elixir*0.12)

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self._up_attributes_prophet(23, 0, 100)
        self.print_for_special_ability_necromancer_prophet()
        enemy_fighter.take_damage(0, 0, 0, 0)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        self.health += 10
        self.energy += 4
        self._up_attributes_prophet(0, 4, 10)
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.4)

    def print_for_special_ability_necromancer_prophet(self):
        print(f'{self.name} использует восстановление и увеличение силы')


prophet = Prophet('Пророк', 240, 140, 95, 'Волшебный посох', 2700, 50)
