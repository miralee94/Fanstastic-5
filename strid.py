from random import randint
import random
from karaktärer import hero_choose, Riddaren, Tjuven, Trollkarlen
from karaktärer import Big_Spider, Skeleton, Troll, Orc


class Strid:
    def __init__(self):

        #self.monster = {'name': 'jättespindel', 'initiativ': 7, 'tålighet': 5, 'atack': 2, 'smidighet': 3}

        #self.monster_förmågor = [i for i in self.monster.values()]

        # self.fighters = ['riddare', 'jättespindel']

        self.heroes_kast = 0
        self.monsters_kast = 0

        self.monster_antal_atack = 0

        self.heroes_antal_kast = []
        self.monsters_antal_kast = []

        self.hero = hero_choose()
        self.monster = 'Big Spider'

    # self.monster_liv = self.monster_förmågor[2]

    def strid_huvud_menu(self):
        huvud_meny = '''Du har hamnat i ett rum med monster, vilket leder till en strid. \nDet ska nu bestämmas vem som ska få börja först'''
        print(huvud_meny)

    def bestäm_turordning(self):
        self.strid_huvud_menu()
        while self.heroes_kast == self.monsters_kast:
            for x in range(self.hero.initiativ):
                self.hero_role_dice(self.heroes_kast)
                self.heroes_antal_kast.append(self.heroes_kast)
            self.heroes_kast = sum(self.heroes_antal_kast)
            print(f'{self.hero.name}: {self.heroes_kast}')
            self.heroes_antal_kast.clear()
            for x in range(self.monster.initiativ):
                self.monster_role_dice(self.monsters_kast)
                self.monsters_antal_kast.append(self.monsters_kast)
            self.monsters_kast = sum(self.monsters_antal_kast)
            print(f'{self.monster.name}: {self.monsters_kast}')
            self.monsters_antal_kast.clear()
            if self.heroes_kast > self.monsters_kast:
                self.hero_choise()
            elif self.heroes_kast < self.monsters_kast:
                self.monster_atack()

    def hero_role_dice(self, heroes_kast):
        self.heroes_kast = randint(1, 6)
        print(f'Hero har slagit: {self.heroes_kast}')

    def monster_role_dice(self, monster_kast):
        self.monsters_kast = randint(1, 6)
        print(f'Monster har slagit: {self.monsters_kast}')

    def check_monster(self):
#        self.monster = 'Big Spider'
        if self.monster == 'Big Spider':
            self.monster = Big_Spider()

        elif self.monster == 'Skeleton':
            self.monster = Skeleton()

        elif self.monster == 'Orc':
            self.monster = Orc()

        elif self.monster == 'Troll':
            self.monster = Troll()


    def check_hero(self):

        if self.hero == 'Riddaren':
            self.hero = Riddaren()
            self.check_monster()
            self.bestäm_turordning()
        elif self.hero == 'Tjuven':
            self.hero = Tjuven()
            self.check_monster()
            self.bestäm_turordning()
        elif self.hero == 'Trollkarlen':
            self.hero = Trollkarlen()
            self.check_monster()
            self.bestäm_turordning()

    def heroes_atack(self):
        print(f'{self.hero.name} försöker attackera')
        print(f'{self.hero.name} Hero kastar tärningar')
        for x in range(self.hero.attack):
            self.hero_role_dice(self.heroes_kast)
            self.heroes_antal_kast.append(self.heroes_kast)
        self.heroes_kast = sum(self.heroes_antal_kast)
        self.heroes_antal_kast.clear()
        print(f'{self.hero.name}: {self.heroes_kast}')

        print('Monster kastar tärningar')
        for x in range(self.monster.smidighet):
            self.monster_role_dice(self.monsters_kast)
            self.monsters_antal_kast.append(self.monsters_kast)
        self.monsters_kast = sum(self.monsters_antal_kast)
        self.monsters_antal_kast.clear()
        print(f'Monster: {self.monsters_kast}')

        if self.heroes_kast > self.monsters_kast:
            self.monster.tålighet = self.monster.tålighet - 1
            print(f'Monster har {self.monster.tålighet} liv kvar')
            if self.monster.tålighet <= 0:

                print(f'{self.monster.name} dog')
            else:
                self.monster_atack()
        else:
            self.monster_atack()

    def monster_atack(self):
#        self.heros_liv = self.hero.tålighet
        print('Monster försöker attackera')
        print('Monster kastar tärningar')
        for x in range(self.monster.attack):
            self.monster_role_dice(self.monsters_kast)
            self.monsters_antal_kast.append(self.monsters_kast)
        self.monsters_kast = sum(self.monsters_antal_kast)
        self.monsters_antal_kast = []
        print(f'Monster: {self.monsters_kast}')

        print(f'{self.hero.name} kastar tärningar')
        for x in range(self.hero.smidighet):
            self.hero_role_dice(self.heroes_kast)
            self.heroes_antal_kast.append(self.heroes_kast)
        self.heroes_kast = sum(self.heroes_antal_kast)
        self.heroes_antal_kast = []
        print(f'{self.hero.name}: {self.heroes_kast}')

        if self.monsters_kast > self.heroes_kast:
            if self.hero.name == 'Riddaren' and self.monster_antal_atack == 0:
                print(
                    'Riddaren använder sin speciella förmåga, attacken blockerad\n Nu är det riddarens tur')
                self.monster_antal_atack += 1
                self.hero_choise()
            else:
                self.hero.tålighet = self.hero.tålighet - 1
                print(f'{self.hero.name} har {self.hero.tålighet} liv kvar')
                if self.hero.tålighet <= 0:
                    print(f'{self.hero.name} dog')
                else:
                    self.hero_choise()
        elif self.monsters_kast < self.heroes_kast:
                print(f'{self.hero.name} blockerar attacken')
                self.monster_antal_atack += 1
                self.hero_choise()


    def hero_choise(self):
        hero_choise_menu = '''Välj mellan följande:
                                1. Försöka atackera
                                2. Försöka fly\n'''
        hero_choice = input(hero_choise_menu)
        if hero_choice == '1':
            self.heroes_atack()
        elif hero_choice == '2':
            self.hero_tries_to_fly()
            if self.hero_tries_to_fly() is True:
                print(f'Hero har lyckats')
            elif self.hero_tries_to_fly() is False:
                print(f'Hero har misslyckats')

#    def strid_loop(self):
#       while self.fighters > 1:

    def hero_tries_to_fly(self):
        procent = self.hero.smidighet * 10
        procent = procent/100
        return random.random() <= procent


#
#def main():
#    foo = Strid()
#    foo.huvud_menu()
#
#
#if __name__ == '__main__':
#   main()
