from fighters_main_class import Fighters
from creatures_castes import Creatures


class Cyborg(Creatures):
    def _up_attributes_cyborg(self, value_defence, value_energy, value_health, value_strenght):
        self.energy += value_energy
        self.defence += value_defence
        self.health += value_health
        self.strenght += value_strenght

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self._up_attributes_cyborg(100, 15, 0, 20)
        self.print_for_special_ability('использовал наноброню')
        enemy_fighter.take_damage(0, 0, 0, 0)

    def attack_knee_blow(self, enemy_fighter):
        self.up_point(5)
        self._up_attributes_cyborg(0, 0, 60, 0)
        self.print_for_attack_knee_blow()
        enemy_fighter.take_damage(25, 5, 6, self.strenght*0.85)


cyborg = Cyborg('Киборг', 300, 125, 65, 'Наноброня', 3600, 200)
