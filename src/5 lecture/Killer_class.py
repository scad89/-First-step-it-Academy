from fighters_main_class import Fighters
from Human_castes import Humans


class Killer(Humans):
    def _up_health_killer(self, value_health):
        self.health += value_health

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.print_for_special_ability_killer(enemy_fighter)
        enemy_fighter.take_damage(0, 0, 30, self.strenght*2)

    def attack_left_arm(self, enemy_fighter):
        self.up_point(1)
        self._up_health_killer(5)
        self.print_for_attack_left_arm()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.4)

    def print_for_special_ability_killer(self, enemy_fighter):
        print(f'{self.name} простреливает колени сопернику {enemy_fighter.name}')


killer = Killer('Киллер', 350, 65, 70, 'Снайперская винтовка', 3000)
