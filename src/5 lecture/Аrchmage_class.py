from fighters_main_class import Fighters
from Mages_castes import Mages


class Аrchmage(Mages):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 100
        self.health += 100
        print(f'{self.name} вызвал огненный дождь.')
        print(
            f'У {enemy_fighter.name} осталось {int(enemy_fighter.health)} очков жизни')
        print()

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        self.health += 100
        enemy_fighter.health -= self.strenght
        print(f'{self.name} использовал/использовала своё оружие, {self.ammo}')
        print(
            f'У {enemy_fighter.name} осталось {int(enemy_fighter.health)} очков жизни')
        print()
