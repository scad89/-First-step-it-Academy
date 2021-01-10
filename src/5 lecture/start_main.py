from human_castes import Humans
from mages_castes import Mages
from creatures_castes import Creatures
from soldier_class import soldier
from ninja_class import ninja
from berserker_class import berserker
from archer_class import archer
from monk_class import monk
from sorceress_class import sorceress
from archmage_class import archmage
from druid_class import druid
from knight_class import knight
from necromancer_class import necromancer
from mutant_class import mutant
from prophet_class import prophet
from killer_class import killer
from cyborg_class import cyborg
from paladin_class import paladin
# import random


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
        fighters.ghoul(fighters)
    elif isinstance(fighters, Creatures):
        fighters.use_rage()


def check_fighters_name_input(fighter):
    return fighter in dict_fighter


def choise_fighter():
    flag_for_fighter = False
    while flag_for_fighter != True:
        fighter = input('>>>> ')
        result = check_fighters_name_input(fighter)
        if result == True:
            flag_for_fighter = True
            return dict_fighter[fighter]
        else:
            print('Вы ввели неверно имя бойца. Попробуйте ещё раз.')


def check_num_for_action():
    flag_num = False
    while flag_num != True:
        num = int(input('>>>>'))
        if 0 <= num <= 7:
            flag_num = True
            return num
        else:
            print('Вы ввели неверное значение для атаки. Попробуйте ещё раз')


def kombat(left_fighter, right_fighter):
    list_action = ['attack_left_arm', 'attack_right_arm', 'attack_left_leg',
                   'attack_right_leg', 'attack_knee_blow', 'attack_headbutt', 'attack_ammo', 'special_ability']
    while not check_finish(left_fighter) and not check_finish(right_fighter):
        #         random.shuffle(list_action)
        check_special_skills_castes(left_fighter)
        print(f'Введите число (0-7), чтобы атаковать {right_fighter.name}: ')
        action_left_fighter = check_num_for_action()
        getattr(left_fighter, list_action[action_left_fighter])(right_fighter)
        check_special_skills_castes(right_fighter)
#        random.shuffle(list_action)
        print(f'Введите число (0-7), чтобы атаковать {left_fighter.name}: ')
        action_right_fighter = check_num_for_action()
        getattr(right_fighter, list_action[action_right_fighter])(left_fighter)


if __name__ == '__main__':
    dict_fighter = {'Солдат': soldier, 'Ниньдзя': ninja, 'Берсерк': berserker, 'Лучница': archer, 'Монах': monk, 'Волшебница': sorceress, 'Верховный маг': archmage, 'Друид': druid, 'Рыцарь': knight, 'Некромант': necromancer, 'Мутант': mutant, 'Пророк': prophet,
                    'Киллер': killer, 'Киборг': cyborg, 'Паладин': paladin}
    print(*dict_fighter.keys(), sep='\n')
    print('Выберите Вашего бойца')
    your_fighter = choise_fighter()
    print('Выберите Вашего соперника')
    your_enemy_fighter = choise_fighter()
    kombat(your_fighter, your_enemy_fighter)
    print(f'{your_fighter.name} набрал {your_fighter.points} очков')
    print(f'{your_enemy_fighter.name} набрал {your_enemy_fighter.points} очков')
