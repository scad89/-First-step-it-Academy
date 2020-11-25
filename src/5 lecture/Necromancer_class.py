from fighters_main_class import Fighters
from Mages_castes import Mages


class Necromancer(Mages):
    def special_ability(self, enemy_fighter):
        skill = input(
            f'Вызвать голема или наложить заклятие на {enemy_fighter.name}? Сдела выбор 1 или 2: ')
        if skill == '1':
            self.golem(enemy_fighter)
        elif skill == '2':
            self.iron_maiden(enemy_fighter)

    def golem(self, enemy_fighter):
        self.up_point(20)
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*2.2
        self.print_for_special_ability_necromancer_golem(enemy_fighter)
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def iron_maiden(self, enemy_fighter):
        damage_defence = 20
        damage_strenght = 20
        damage_energy = 30
        damage_health = 0
        self.print_for_special_ability_necromancer_golem_ironmaiden()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_left_arm(self, enemy_fighter):
        self.up_point(1)
        self.defence += 8
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*0.3
        self.print_for_attack_left_arm()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_necromancer_golem(self, enemy_fighter):
        print(
            f'{self.name} призвал голема и он нанёс сокрушительный удар {enemy_fighter.name}')

    def print_for_special_ability_necromancer_golem_ironmaiden(self):
        print(f'{self.name} использовал заклинание "Iron Maiden"')
