from fighters_main_class import Fighters


class Creatures(Fighters):
    def __init__(self, name, strenght, defence, energy, ammo, health, rage):
        super().__init__(name, strenght, defence, energy, ammo, health)
        self.points = 0
        self.rage = rage
        self._flag_use_rage = True

    def attack_left_arm(self, enemy_fighter):
        self.up_point(6)
        self.print_for_attack_left_arm()
        enemy_fighter.take_damage(5, 0, 2, self.strenght*0.4)

    def attack_right_arm(self, enemy_fighter):
        self.up_point(7)
        self.print_for_attack_right_arm()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.6)

    def use_rage(self):
        if self.health < 400 and self._flag_use_rage == True:
            self.strenght += self.rage
            self._flag_use_rage = False
            self.print_for_use_rage()

    def print_for_use_rage(self):
        print(
            f'{self.name} использует "Ярость" для увеличения атаки')
        print()
