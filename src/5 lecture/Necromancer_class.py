from fighters_main_class import Fighters
from Mages_castes import Mages


class Necromancer(Mages):
    def _up_defence_necromancer(self, value_defence):
        self.defence += (value_defence+self.elixir*0.1)

    def special_ability(self, enemy_fighter):
        skill = input(
            f'Вызвать голема или наложить заклятие на {enemy_fighter.name}? Сдела выбор 1 или 2: ')
        if skill == '1':
            self.golem(enemy_fighter)
        elif skill == '2':
            self.iron_maiden(enemy_fighter)

    def golem(self, enemy_fighter):
        self.up_point(20)
        self.print_for_special_ability_necromancer_golem(enemy_fighter)
        enemy_fighter.take_damage(0, 0, 0, self.strenght*2.2)

    def iron_maiden(self, enemy_fighter):
        self.print_for_special_ability_necromancer_golem_ironmaiden()
        enemy_fighter.take_damage(20, 20, 30, 0)

    def attack_left_arm(self, enemy_fighter):
        self.up_point(1)
        self._up_defence_necromancer(8)
        self.print_for_attack_left_arm()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.3)

    def print_for_special_ability_necromancer_golem(self, enemy_fighter):
        print(
            f'{self.name} призвал голема и он нанёс сокрушительный удар {enemy_fighter.name}')

    def print_for_special_ability_necromancer_golem_ironmaiden(self):
        print(f'{self.name} использовал заклинание "Iron Maiden"')


necromancer = Necromancer('Некромант', 280, 70, 95,
                          'Костянной посох', 3000, 50)
