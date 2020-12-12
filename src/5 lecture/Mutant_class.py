from fighters_main_class import Fighters
from Creatures_castes import Creatures


class Mutant(Creatures):
    def _up_attributes_mutant(self, value_strenght, value_health):
        self.strenght += (value_strenght+(self.rage*0.1))
        self.health += (value_health+self.rage*0.2)

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.print_for_special_ability_mutant(enemy_fighter)
        enemy_fighter.take_damage(0, 0, 0, self.strenght*2)

    def attack_left_leg(self, enemy_fighter):
        self.up_point(3)
        self._up_attributes_mutant(10, 60)
        self.print_for_attack_left_leg()
        enemy_fighter.take_damage(5, 3, 0, self.strenght*0.5)

    def print_for_special_ability_mutant(self, enemy_fighter):
        print(f'{self.name} проткнул {enemy_fighter.name} своими щупальцами')


mutant = Mutant('Мутант', 270, 80, 70, 'Пулемёт', 4500, 180)
