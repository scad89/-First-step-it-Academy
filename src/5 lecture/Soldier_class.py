from fighters_main_class import Fighters
from Human_castes import Humans


class Soldier(Humans):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.print_for_special_ability_soldier()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*2.5)

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        self.print_for_attack_ammo()
        enemy_fighter.take_damage(30, 5, 10, self.strenght*1.5)

    def print_for_special_ability_soldier(self):
        print(f'{self.name} бросил гранату')


soldier = Soldier('Солдат', 300, 80, 70, 'Атомат', 3000)
