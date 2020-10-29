from fighters_main_class import Fighters
from fighter_castes import *


class Soldier(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 110
        print(f'{self.name} бросил гранату')
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


class Berserker(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 220
        print(
            f'{self.name} наносит удар топором {enemy_fighter.name}')
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


class Archer(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 170
        print(
            f'{self.name} производит выстрел взрывающейся стрелой {enemy_fighter.name}')
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


class Monk(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.strenght += 5
        self.defence += 10
        self.health += 100
        print(f'{self.name} прочитал молитву и увеличил свои атрибуты')
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


class Sorceress(Mages):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 100
        enemy_fighter.strenght -= 5
        enemy_fighter.defence -= 5
        enemy_fighter.energy -= 15
        print(f'{self.name} призывает ледяной шторм')
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


class Knight(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 200
        print(f'{self.name} проткнул копьём {enemy_fighter.name}')
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


class Prophet(Mages):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.strenght += 15
        self.health += 100
        print(f'{self.name} использует восстановление и увеличение силы')
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


class Killer(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 80
        enemy_fighter.energy -= 30
        print(f'{self.name} простреливает колени {enemy_fighter.name}')
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


class Cyborg(Creatures):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.energy += 12
        self.defence += 20
        print(f'{self.name} использовал наноброню')
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


class Paladin(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.strenght += 5
        enemy_fighter.health -= 120
        print(f'{self.name} вызвал ауру и нанёс урон {enemy_fighter.name}')
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
