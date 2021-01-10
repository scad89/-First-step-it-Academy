from fighters_main_class import Fighters


class Humans(Fighters):
    def __init__(self, name, strenght, defence, energy, ammo, health):
        super().__init__(name, strenght, defence, energy, ammo, health)
        self.points = 0
        self.armor = self.points
        self._flag_up_armor = True
        self._flag_up_strengh = True

    def _up_strenght_human(self, value_strenght):
        self.strenght += (value_strenght+(self.energy*2))

    def up_armor_human(self):
        if self.health < 400 and self._flag_up_armor == True:
            self.defence += self.armor
            self._flag_up_armor = False
            self.print_for_up_armor_human()

    def up_strenght(self):
        if self.health < 400 and self._flag_up_strengh == True:
            self._up_strenght_human(150)
            self._flag_up_strengh = False
            self.print_for_up_strenght()

    def attack_right_leg(self, enemy_fighter):
        self.up_point(5)
        self.print_for_attack_right_leg()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*0.8)

    def print_for_up_armor_human(self):
        print(f'Броня {self.name} повышена на {self.points} очков')
        print()

    def print_for_up_strenght(self):
        print(f'Атака {self.name} увеличина')
        print()
