from fighters_main_class import Fighters
from Mages_castes import Mages


class Prophet(Mages):
    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.strenght += 15
        self.health += 100
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = 0
        self.print_for_special_ability_necromancer_prophet()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        self.health += 10
        self.energy += 4
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 0
        damage_health = self.strenght*0.4
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_special_ability_necromancer_prophet(self):
        print(f'{self.name} использует восстановление и увеличение силы')
