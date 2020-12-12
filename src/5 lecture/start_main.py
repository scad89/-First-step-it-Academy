from fighters_main_class import Fighters
from Human_castes import Humans
from Mages_castes import Mages
from Creatures_castes import Creatures
from Soldier_class import soldier
from Ninja_class import ninja
from Berserker_class import berserker
from Archer_class import archer
from Monk_class import monk
from Sorceress_class import sorceress
from Аrchmage_class import archmage
from Druid_class import druid
from Knight_class import knight
from Necromancer_class import necromancer
from Mutant_class import mutant
from Prophet_class import prophet
from Killer_class import killer
from Cyborg_class import cyborg
from Paladin_class import paladin
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
        fighters.ghoul(fighters)
    elif isinstance(fighters, Creatures):
        fighters.use_rage()


def kombat(left_fighter, right_fighter):
    list_action = ['attack_left_arm', 'attack_right_arm', 'attack_left_leg',
                   'attack_right_leg', 'attack_knee_blow', 'attack_headbutt', 'attack_ammo', 'special_ability']
    while not check_finish(left_fighter) and not check_finish(right_fighter):
        random.shuffle(list_action)
        check_special_skills_castes(left_fighter)
        action_left_fighter = int(
            input(f'Введите число (1-8), чтобы атаковать {right_fighter.name}: '))
        getattr(left_fighter, list_action[action_left_fighter])(right_fighter)
        check_special_skills_castes(right_fighter)
        random.shuffle(list_action)
        action_right_fighter = int(
            input(f'Введите число (1-8), чтобы атаковать {left_fighter.name}: '))
        getattr(right_fighter, list_action[action_right_fighter])(left_fighter)


if __name__ == '__main__':
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
