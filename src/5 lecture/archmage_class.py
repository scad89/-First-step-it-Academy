from fighters_main_class import Fighters
from mages_castes import Mages


class Аrchmage(Mages):
    def _up_health_archmage(self, value):
        self.health += value

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self._up_health_archmage(100)
        self.print_for_special_ability('вызвал огненный дождь')
        enemy_fighter.take_damage(0, 0, 0, self.strenght*2)

    def attack_headbutt(self, enemy_fighter):
        self.up_point(5)
        self.print_for_attack_headbutt()
        enemy_fighter.take_damage(3, 3, 3, self.strenght*0.7)


archmage = Аrchmage('Верховный маг', 340, 80, 95, 'Волшебный жезл', 3300, 50)
