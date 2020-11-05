from fighters_main_class import Fighters
from Human_castes import Humans


class Ninja(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 150
        print(
            f'{self.name} бросает дымовую гранату и наносит удар катаной в уязвимое место')
        print(
            f'У {enemy_fighter.name} осталось {int(enemy_fighter.health)} очков жизни')
        print()

    def attack_right_leg(self, enemy_fighter):
        self.up_point(4)
        enemy_fighter.health -= (self.strenght*0.8)
        print(f'{self.name} нанёс/нанесла удар правой ногой')
        print(
            f'У {enemy_fighter.name} осталось {int(enemy_fighter.health)} очков жизни')
        print()
