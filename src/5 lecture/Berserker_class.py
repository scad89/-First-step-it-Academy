from fighters_main_class import Fighters
from human_castes import Humans


class Berserker(Humans):
    def _up_strenght_and_energy(self, value_strenght, value_energy):
        self.strenght += value_strenght
        self.energy += value_energy

    def special_ability(self, enemy_fighter):
        self.up_point(20)
        self.print_for_special_ability(
            f'наносит удар топором {enemy_fighter.name}')
        enemy_fighter.take_damage(0, 0, 20, self.strenght*2)

    def attack_ammo(self, enemy_fighter):
        self.up_point(8)
        self._up_strenght_and_energy(15, 10)
        self.print_for_attack_ammo()
        enemy_fighter.take_damage(0, 0, 0, self.strenght*1.7)


berserker = Berserker('Берсерк', 320, 60, 70, 'Два меча', 3600)
