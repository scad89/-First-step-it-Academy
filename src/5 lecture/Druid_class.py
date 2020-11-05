from fighters_main_class import Fighters
from Mages_castes import Mages


class Druid(Mages):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 120
        self.strenght += 15
        self.defence += 8
        self.health += 50
        print(f'{self.name} превратился в волка и сильно ранил {enemy_fighter.name}')
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
