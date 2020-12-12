from fighters_main_class import Fighters
from Human_castes import Humans


class Ninja(Humans):
    def _up_attributes_ninja(self, value_health):
        self.health += (value_health+self.energy*0.2)

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.print_for_special_ability_ninja()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*2)

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        self._up_attributes_ninja(50)
        self.print_for_attack_ammo()
        enemy_fighter.take_damage(12, 3, 8, self.strenght*1.4)

    def print_for_special_ability_ninja(self):
        print(
            f'{self.name} бросает дымовую гранату и наносит удар катаной в уязвимое место')


ninja = Ninja('Ниньдзя', 340, 40, 70, 'Катана', 2700)
