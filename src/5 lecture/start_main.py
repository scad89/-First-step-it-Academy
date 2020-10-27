from fighters_main_class import Fighters
import random


class Soldier(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 110
        print(f'{self.name} бросил гранату')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Ninja(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 150
        print(
            f'{self.name} бросает дымовую гранату и наносит удар катаной в уязвимое место')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Berserker(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 220
        print(
            f'{self.name} наносит удар топором {enemy_fighter.name}')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Archer(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 170
        print(
            f'{self.name} производит выстрел взрывающейся стрелой {enemy_fighter.name}')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Monk(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.strenght += 5
        self.defence += 10
        self.health += 100
        print(f'{self.name} прочитал молитву и увеличил свои атрибуты')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Sorceress(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 100
        enemy_fighter.strenght -= 5
        enemy_fighter.defence -= 5
        enemy_fighter.energy -= 15
        print(f'{self.name} призывает ледяной шторм')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Аrchmage(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 100
        self.health += 100
        print(f'{self.name} вызвал огненный дождь.')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Druid(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 120
        self.strenght += 15
        self.defence += 8
        self.health += 50
        print(f'{self.name} превратился в волка и сильно ранил {enemy_fighter.name}')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Knight(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 200
        print(f'{self.name} проткнул копьём {enemy_fighter.name}')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Necromancer(Fighters):
    def special_ability(self, enemy_fighter):
        skill = input(
            f'Вызвать голема или наложить заклятие на {enemy_fighter.name}? Сдела выбор 1 или 2: ')
        if skill == '1':
            self.up_point(20)
            enemy_fighter.health -= 160
            print(
                f'{self.name} призвал голема и он нанёс сокрушительный удар {enemy_fighter.name}')
        elif skill == '2':
            self.up_point(20)
            enemy_fighter.strenght -= 20
            enemy_fighter.defence -= 20
            enemy_fighter.energy -= 30
            print(f'{self.name} использовал заклинание "Iron Maiden"')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Mutant(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 150
        print(f'{self.name} проткнул {enemy_fighter.name} своими щупальцами')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Prophet(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.strenght += 15
        self.health += 100
        print(f'{self.name} использует восстановление и увеличение силы')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Killer(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        enemy_fighter.health -= 80
        enemy_fighter.energy -= 30
        print(f'{self.name} простреливает колени {enemy_fighter.name}')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Cyborg(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.energy += 12
        self.defence += 20
        print(f'{self.name} использовал наноброню')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


class Paladin(Fighters):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.strenght += 5
        enemy_fighter.health -= 120
        print(f'{self.name} вызвал ауру и нанёс урон {enemy_fighter.name}')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')


def check_finish(fighter):
    if fighter.health < 0:
        print(f'Боец {fighter.name} убит.')

        return True
    return False


def kombat(left_fighter, right_fighter, *list_action):
    while not check_finish(left_fighter) and not check_finish(right_fighter):
        list_action = ['attack_left_arm', 'attack_right_arm', 'attack_left_leg',
                       'attack_right_leg', 'attack_knee_blow', 'attack_headbutt', 'attack_ammo', 'special_ability']
        random.shuffle(list_action)
        action_left_fighter = int(
            input(f'Введите число (0-7), чтобы атаковать {right_fighter.name}: '))
        if list_action[action_left_fighter] == 'attack_left_arm':
            left_fighter.attack_left_arm(right_fighter)
        elif list_action[action_left_fighter] == 'attack_right_arm':
            left_fighter.attack_right_arm(right_fighter)
        elif list_action[action_left_fighter] == 'attack_left_leg':
            left_fighter.attack_left_leg(right_fighter)
        elif list_action[action_left_fighter] == 'attack_right_leg':
            left_fighter.attack_right_leg(right_fighter)
        elif list_action[action_left_fighter] == 'attack_knee_blow':
            left_fighter.attack_knee_blow(right_fighter)
        elif list_action[action_left_fighter] == 'attack_headbutt':
            left_fighter.attack_headbutt(right_fighter)
        elif list_action[action_left_fighter] == 'attack_ammo':
            left_fighter.attack_ammo(right_fighter)
        elif list_action[action_left_fighter] == 'special_ability':
            left_fighter.special_ability(right_fighter)
        random.shuffle(list_action)
        action_right_fighter = int(
            input(f'Введите число (0-7), чтобы атаковать {left_fighter.name}: '))
        if list_action[action_right_fighter] == 'attack_left_arm':
            right_fighter.attack_left_arm(left_fighter)
        elif list_action[action_right_fighter] == 'attack_right_arm':
            right_fighter.attack_right_arm(left_fighter)
        elif list_action[action_right_fighter] == 'attack_left_leg':
            right_fighter.attack_left_leg(left_fighter)
        elif list_action[action_right_fighter] == 'attack_right_leg':
            right_fighter.attack_right_leg(left_fighter)
        elif list_action[action_right_fighter] == 'attack_knee_blow':
            right_fighter.attack_knee_blow(left_fighter)
        elif list_action[action_right_fighter] == 'attack_headbutt':
            right_fighter.attack_headbutt(left_fighter)
        elif list_action[action_right_fighter] == 'attack_ammo':
            right_fighter.attack_ammo(left_fighter)
        elif list_action[action_right_fighter] == 'special_ability':
            right_fighter.special_ability(left_fighter)


soldier = Soldier('Солдат', 100, 80, 100, 'Атомат', 1000)
ninja = Ninja('Ниньдзя', 120, 40, 100, 'Катана', 900)
berserker = Berserker('Берсерк', 110, 60, 100, 'Два меча', 1200)
archer = Archer('Лучница', 130, 40, 100, 'Лук', 900)
monk = Monk('Монах', 100, 60, 100, 'Боевое кадило', 1000)
sorceress = Sorceress('Волшебница', 110, 50, 150, 'Посох', 1000)
archmage = Аrchmage('Верховный маг', 120, 80, 150, 'Волшебный жезл', 1100)
druid = Druid('Друид', 80, 120, 150, 'Коготь зверя', 900)
knight = Knight('Рыцарь', 50, 150, 100, 'Меч', 1150)
necromancer = Necromancer('Некромант', 90, 70, 150, 'Костянной посох', 1000)
mutant = Mutant('Мутант', 85, 80, 100, 'Пулемёт', 1500)
prophet = Prophet('Пророк', 70, 140, 150, 'Волшебный посох', 900)
killer = Killer('Киллер', 125, 65, 100, 'Снайперская винтовка', 1000)
cyborg = Cyborg('Киборг', 100, 125, 90, 'Наноброня', 1200)
paladin = Paladin('Паладин', 100, 130, 100, 'Святой посох', 1100)

dict_fighter = {'Солдат': soldier, 'Ниндзья': ninja, 'Берсерк': berserker, 'Лучница': archer, 'Монах': monk, 'Волшебница': sorceress, 'Верховный маг': archmage, 'Друид': druid, 'Рыцарь': knight, 'Некромант': necromancer, 'Мутант': mutant, 'Пророк': prophet,
                'Киллер': killer, 'Киборг': cyborg, 'Паладин': paladin}
print(*dict_fighter.keys(), sep='\n')
choise_left_fighter = input('Выберите Вашего бойца: ')
left_fighter = dict_fighter[choise_left_fighter]
choise_right_fighter = input('Выберите Вашего соперника: ')
right_fighter = dict_fighter[choise_right_fighter]
kombat(left_fighter, right_fighter)
print(f'Вы набрали {left_fighter.points} очков')
