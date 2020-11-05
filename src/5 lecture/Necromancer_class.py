from fighters_main_class import Fighters
from Mages_castes import Mages


class Necromancer(Mages):
    def special_ability(self, enemy_fighter):
        skill = input(
            f'Вызвать голема или наложить заклятие на {enemy_fighter.name}? Сдела выбор 1 или 2: ')
        if skill == '1':
            self.up_point(20)
            enemy_fighter.health -= 160
            print(
                f'{self.name} призвал голема и он нанёс сокрушительный удар {int(enemy_fighter.health)}')
            print()
        elif skill == '2':
            self.up_point(20)
            enemy_fighter.strenght -= 20
            enemy_fighter.defence -= 20
            enemy_fighter.energy -= 30
            print(f'{self.name} использовал заклинание "Iron Maiden"')
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
