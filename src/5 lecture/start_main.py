from fighters_main_class import Fighters
from Human_castes import Humans
from Mages_castes import Mages
from Creatures_castes import Creatures
from Soldier_class import *
from Ninja_class import *
from Berserker_class import *
from Archer_class import *
from Monk_class import *
from Sorceress_class import *
from Аrchmage_class import *
from Druid_class import *
from Knight_class import *
from Necromancer_class import *
from Mutant_class import *
from Prophet_class import *
from Killer_class import *
from Cyborg_class import *
from Paladin_class import *
import random


def check_finish(fighter):
    if fighter.health < 0:
        print(f'Боец {fighter.name} убит.')
        return True
    return False


def check_special_skills_castes(fighters):
    if isinstance(fighters, Humans):
        fighters.up_armor_human()
        fighters.up_strenght()
    elif isinstance(fighters, Mages):
        fighters.recovery()
        fighters.ghoul()
    elif isinstance(fighters, Creatures):
        fighters.use_rage()


def kombat(left_fighter, right_fighter):
    list_action = ['attack_left_arm', 'attack_right_arm', 'attack_left_leg',
                   'attack_right_leg', 'attack_knee_blow', 'attack_headbutt', 'attack_ammo', 'special_ability']
    while not check_finish(left_fighter) and not check_finish(right_fighter):
        random.shuffle(list_action)
        check_special_skills_castes(left_fighter)
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
        check_special_skills_castes(right_fighter)
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


if __name__ == '__main__':
    soldier = Soldier('Солдат', 150, 80, 70, 'Атомат', 2000)
    ninja = Ninja('Ниньдзя', 170, 40, 70, 'Катана', 1800)
    berserker = Berserker('Берсерк', 160, 60, 70, 'Два меча', 2400)
    archer = Archer('Лучница', 180, 40, 70, 'Лук', 1800)
    monk = Monk('Монах', 150, 60, 70, 'Боевое кадило', 2000)
    sorceress = Sorceress('Волшебница', 160, 50, 95, 'Посох', 2000, 50)
    archmage = Аrchmage('Верховный маг', 170, 80, 95,
                        'Волшебный жезл', 2200, 50)
    druid = Druid('Друид', 130, 120, 95, 'Коготь зверя', 1900, 50)
    knight = Knight('Рыцарь', 100, 150, 70, 'Меч', 2300)
    necromancer = Necromancer('Некромант', 140, 70, 95,
                              'Костянной посох', 2000, 50)
    mutant = Mutant('Мутант', 135, 80, 70, 'Пулемёт', 3000, 30)
    prophet = Prophet('Пророк', 120, 140, 95, 'Волшебный посох', 1800, 50)
    killer = Killer('Киллер', 175, 65, 70, 'Снайперская винтовка', 2000)
    cyborg = Cyborg('Киборг', 150, 125, 65, 'Наноброня', 2400, 30)
    paladin = Paladin('Паладин', 150, 130, 70, 'Святой посох', 2200)

    dict_fighter = {'Солдат': soldier, 'Ниньдзя': ninja, 'Берсерк': berserker, 'Лучница': archer, 'Монах': monk, 'Волшебница': sorceress, 'Верховный маг': archmage, 'Друид': druid, 'Рыцарь': knight, 'Некромант': necromancer, 'Мутант': mutant, 'Пророк': prophet,
                    'Киллер': killer, 'Киборг': cyborg, 'Паладин': paladin}
    print(*dict_fighter.keys(), sep='\n')
    choise_left_fighter = input('Выберите Вашего бойца: ')
    your_fighter = dict_fighter[choise_left_fighter]
    choise_right_fighter = input('Выберите Вашего соперника: ')
    your_enemy_fighter = dict_fighter[choise_right_fighter]
    kombat(your_fighter, your_enemy_fighter)
    print(f'{your_fighter.name} набрал {your_fighter.points} очков')
    print(f'{your_enemy_fighter.name} набрал {your_enemy_fighter.points} очков')
