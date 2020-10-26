class Fighters:
    def __init__(self, name, strenght, defence, energy, ammo, health):
        self.name = name
        self.strenght = strenght
        self.defence = defence
        self.energy = energy
        self.ammo = ammo
        self.health = health
        self.points = 0

    def up_point(self, count_points):
        self.points += count_points

    def __drop_energy(self, count):
        self.energy -= count
        if 40 < self.energy < 60:
            self.strenght -= (self.strenght*0.05)
            print(f'У {self.name} атака снижена на 5%')
        elif 20 < self.energy < 40:
            self.strenght -= (self.strenght*0.05)
            print(f'У {self.name} атака снижена на 10%')
        elif self.energy < 20:
            self.strenght -= (self.strenght*0.05)
            print(f'У {self.name} атака снижена на 15%')

    def attack_left_arm(self, enemy_fighter):
        self.up_point(1)
        self.__drop_energy(1)
        enemy_fighter.health -= (self.strenght -
                                 ((enemy_fighter.health+enemy_fighter.defence)*0.01*4))
        print(f'{self.name} нанёс/нанесла удар левой рукой')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')

    def attack_right_arm(self, enemy_fighter):
        self.up_point(2)
        self.__drop_energy(2)
        enemy_fighter.health -= (self.strenght -
                                 ((enemy_fighter.health+enemy_fighter.defence)*0.01*2))
        print(f'{self.name} нанёс/нанесла удар правой рукой')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')

    def attack_left_leg(self, enemy_fighter):
        self.up_point(3)
        self.__drop_energy(3)
        enemy_fighter.health -= (self.strenght -
                                 ((enemy_fighter.health+enemy_fighter.defence)*0.01*5))
        print(f'{self.name} нанёс/нанесла удар левой ногой')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')

    def attack_right_leg(self, enemy_fighter):
        self.up_point(4)
        self.__drop_energy(4)
        enemy_fighter.health -= (self.strenght -
                                 ((enemy_fighter.health+enemy_fighter.defence)*0.01*3))
        print(f'{self.name} нанёс/нанесла удар правой ногой')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')

    def attack_knee_blow(self, enemy_fighter):
        self.up_point(5)
        self.__drop_energy(4)
        enemy_fighter.health -= (self.strenght -
                                 ((enemy_fighter.health+enemy_fighter.defence)*0.01*0.5))
        print(f'{self.name} нанёс/нанесла удар коленом')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')

    def attack_headbutt(self, enemy_fighter):
        self.up_point(5)
        self.__drop_energy(3)
        enemy_fighter.health -= (self.strenght -
                                 ((enemy_fighter.health+enemy_fighter.defence)*0.01*0.7))
        print(f'{self.name} нанёс/нанесла удар головой')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        self.__drop_energy(10)
        enemy_fighter.health -= self.strenght
        print(f'{self.name} использовал/использовала своё оружие, {self.ammo}')
        print(f'У {enemy_fighter.name} осталось {enemy_fighter.health} очков жизни')

    def special_ability(self, enemy_fighter):
        self.__drop_energy(15)
