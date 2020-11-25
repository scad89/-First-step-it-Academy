from fighters_main_class import Fighters


class Mages(Fighters):
    def __init__(self, name, strenght, defence, energy, ammo, health, elixir):
        self.name = name
        self.strenght = strenght
        self.defence = defence
        self.energy = energy
        self.ammo = ammo
        self.health = health
        self.points = 0
        self.elixir = elixir
        self.flag_recovery = True
        self.flag_ghoul = True

    def recovery(self):
        if self.energy < 10 and self.flag_recovery == True:
            self.energy += self.elixir
            self.flag_recovery = False
            self.print_for_recovery()

    def ghoul(self):
        if self.health < 200 and self.flag_ghoul == True:
            self.health += 250
            self.flag_ghoul = False
            self.print_for_ghoul()

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        damage_defence = 0
        damage_strenght = 0
        damage_energy = 5
        damage_health = self.strenght*1.5
        self.print_for_attack_ammo()
        enemy_fighter.take_damage(
            damage_defence, damage_strenght, damage_energy, damage_health)

    def print_for_recovery(self):
        print(f'{self.name} использовал(а) эликсир для восстановления')
        print()

    def print_for_ghoul(self):
        print(
            f'{self.name} использует вампиризм для восстановления очков здоровья')
        print()
