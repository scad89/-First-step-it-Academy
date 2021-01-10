from fighters_main_class import Fighters
from human_castes import Humans


class Monk(Humans):
    def _up_attributes_monk(self, value_strenght, value_defence, value_health, value_energy):
        self.strenght += value_strenght
        self.defence += value_defence
        self.health += value_health
        self.energy += value_energy

    def special_ability(self, enemy_fighter):
        self._up_attributes_monk(10, 10, 100, 0)
        self.print_for_special_ability(
            'прочитал молитву и увеличил свои атрибуты')
        enemy_fighter.take_damage(0, 0, 0, 0)

    def attack_left_arm(self, enemy_fighter):
        self.up_point(1)
        self._up_attributes_monk(0, 0, 0, 3)
        self.print_for_attack_left_arm()
        enemy_fighter.take_damage(5, 0, 1, self.strenght*0.4)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        self._up_attributes_monk(0, 0, 0, 5)
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(7, 0, 2, self.strenght*0.6)


monk = Monk('Монах', 290, 60, 70, 'Боевое кадило', 3000)
