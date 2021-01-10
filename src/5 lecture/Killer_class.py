from fighters_main_class import Fighters
from human_castes import Humans


class Killer(Humans):
    def _up_health_killer(self, value_health):
        self.health += value_health

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.print_for_special_ability(
            f'простреливает колени сопернику {enemy_fighter.name}')
        enemy_fighter.take_damage(0, 0, 30, self.strenght*2)

    def attack_left_arm(self, enemy_fighter):
        self.up_point(1)
        self._up_health_killer(5)
        self.print_for_attack_left_arm()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.4)


killer = Killer('Киллер', 350, 65, 70, 'Снайперская винтовка', 3000)
