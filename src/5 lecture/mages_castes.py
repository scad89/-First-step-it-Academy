from fighters_main_class import Fighters


class Mages(Fighters):
    def __init__(self, name, strenght, defence, energy, ammo, health, elixir):
        super().__init__(name, strenght, defence, energy, ammo, health)
        self.points = 0
        self.elixir = elixir
        self._flag_recovery = True
        self._flag_ghoul = True

    def _up_attributes_mages(self, value_health, value_strenght):
        self.health += value_health
        self.strenght += value_strenght

    def recovery(self):
        if self.energy < 10 and self._flag_recovery == True:
            self.energy += self.elixir
            self._up_attributes_mages(50, 30)
            self.strenght += 30
            self._flag_recovery = False
            self.print_for_recovery()

    def ghoul(self, enemy_fighter):
        if self.health < 400 and self._flag_ghoul == True:
            self._up_attributes_mages(800, 0)
            self._flag_ghoul = False
            self.print_for_ghoul()
            enemy_fighter.take_damage(0, 0, 5, 400)

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        self.print_for_attack_ammo()
        enemy_fighter.take_damage(0, 0, 5, self.strenght*1.5)

    def print_for_recovery(self):
        print(f'{self.name} использовал(а) эликсир для восстановления')
        print()

    def print_for_ghoul(self):
        print(
            f'{self.name} использует вампиризм для восстановления очков здоровья')
        print()
