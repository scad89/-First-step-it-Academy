from fighters_main_class import Fighters
from Human_castes import Humans


class Knight(Humans):
    def _up_strenght_knight(self, value_strenght):
        self.strenght += value_strenght

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.print_for_special_ability_knight(enemy_fighter)
        enemy_fighter.take_damage(0, 0, 0, self.strenght*2)

    def attack_headbutt(self, enemy_fighter):
        self.up_point(5)
        self._up_strenght_knight(5)
        self.print_for_attack_headbutt()
        enemy_fighter.take_damage(10, 0, 0, self.strenght*0.8)

    def print_for_special_ability_knight(self, enemy_fighter):
        print(f'{self.name} проткнул копьём {enemy_fighter.name}')


knight = Knight('Рыцарь', 200, 150, 70, 'Меч', 3600)
