from fighters_main_class import Fighters
from Creatures_castes import Creatures


class Mutant(Creatures):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 150
        print(f'{self.name} проткнул {enemy_fighter.name} своими щупальцами')
        print(
            f'У {enemy_fighter.name} осталось {int(enemy_fighter.health)} очков жизни')
        print()

    def attack_left_arm(self, enemy_fighter):
        self.up_point(1)
        enemy_fighter.health -= (self.strenght*0.2)
        print(f'{self.name} нанёс/нанесла удар левой рукой')
        print(
            f'У {enemy_fighter.name} осталось {int(enemy_fighter.health)} очков жизни')
        print()

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        enemy_fighter.health -= (self.strenght*0.2)
        print(f'{self.name} нанёс/нанесла удар правой рукой')
        print(
            f'У {enemy_fighter.name} осталось {int(enemy_fighter.health)} очков жизни')
        print()
