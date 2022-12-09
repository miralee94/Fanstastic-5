from random import randint
#import Riddare
#import Jättespindel
class Strid:

    def __init__(self):
        #self.hero =  self.check_hero()
        #self.monster = self.check_monster()

        self.hero = {'name': 'riddare', 'initiativ': 5, 'tålighet': 9, 'atack': 6, 'smidighet': 4}
        self.monster = {'name': 'jättespindel', 'initiativ': 7, 'tålighet': 5, 'atack': 2, 'smidighet': 3}

        self.hero_förmågor = [i for i in self.hero.values()]
        self.monster_förmågor = [i for i in self.monster.values()]

        self.fighters = ['riddare', 'jättespindel']

        self.heroes_kast = 0
        self.monsters_kast = 0

        self.monster_antal_atack = 0

        self.heroes_antal_kast = []
        self.monsters_antal_kast = []

        self.monster_liv = self.monster_förmågor[2]

    def huvud_menu(self):
        huvud_meny = '''Du har hamnat i ett rum med monster, vilket leder till en strid. \nDet ska nu bestämmas vem som ska få börja först'''
        print(huvud_meny)
        self.bestäm_turordning()

    def bestäm_turordning(self):
        while self.heroes_kast == self.monsters_kast:
            self.hero_role_dice(self.heroes_kast)
            self.monster_role_dice(self.monsters_kast)
            if self.heroes_kast > self.monsters_kast:
                self.hero_choise()
            elif self.heroes_kast < self.monsters_kast:
                self.monster_atack()

    def hero_role_dice(self, heroes_kast):
        self.heroes_kast = randint(1, 6)
        print(f'Hero har slagit: {self.heroes_kast}')

    def monster_role_dice(self,monster_kast):
        self.monsters_kast = randint(1, 6)
        print(f'Monster har slagit: {self.monsters_kast}')

    #def check_monster(self):
    #    if self.monster == class Jättespindel:

    #def check_hero(self):
    #    if self.hero == class Riddare:


    def heroes_atack(self):
        print('Hero attackerar')
        print('Hero kastar tärningar')
        for x in range(self.hero_förmågor[3]):
            self.hero_role_dice(self.heroes_kast)
            self.heroes_antal_kast.append(self.heroes_kast)
        self.heroes_kast = sum(self.heroes_antal_kast)
        self.heroes_antal_kast = []
        print(f'Hero: {self.heroes_kast}')

        print('Monster kastar tärningar')
        for x in range(self.monster_förmågor[4]):
            self.monster_role_dice(self.monsters_kast)
            self.monsters_antal_kast.append(self.monsters_kast)
        self.monsters_kast = sum(self.monsters_antal_kast)
        self.monsters_antal_kast = []
        print(f'Monster: {self.monsters_kast}')

        if self.heroes_kast > self.monsters_kast:
            self.monster_liv = self.monster_liv - 1
            if self.monster_liv <= 0:
                self.monster.clear()
                print('Jättespindel dog')
            else:
                self.monster_atack()
        else:
            self.monster_atack()

    def monster_atack(self):
        print('Monster attackerar')
        print('Monster kastar tärningar')
        for x in range(self.monster_förmågor[3]):
            self.monster_role_dice(self.monsters_kast)
            self.monsters_antal_kast.append(self.monsters_kast)
        self.monsters_kast = sum(self.monsters_antal_kast)
        self.monsters_antal_kast = []
        print(f'Monster: {self.monsters_kast}')

        print('Hero kastar tärningar')
        for x in range(self.hero_förmågor[4]):
            self.hero_role_dice(self.heroes_kast)
            self.heroes_antal_kast.append(self.heroes_kast)
        self.heroes_kast = sum(self.heroes_antal_kast)
        self.heroes_antal_kast = []
        print(f'hero: {self.heroes_kast}')

        if self.monsters_kast > self.heroes_kast:
            if self.hero_förmågor[0] == 'riddare' and self.monster_antal_atack == 0:
                print('Riddaren använder sin speciella förmåga, attacken blockerad\n Nu är det riddarens tur')
                self.monster_antal_atack +=1
                self.hero_choise()
            else:
                riddarens_liv = self.hero_förmågor[2] - 1
                if riddarens_liv <=0:
                    self.hero.clear()
                    print('Riddaren dog')
                else:
                    self.hero_choise()
        elif self.monsters_kast < self.heroes_kast:
            if self.hero_förmågor[0] == 'riddare' and self.monster_antal_atack == 0:
                print('Riddaren använder sin speciella förmåga, attacken blockerad')
                self.monster_antal_atack +=1
                self.hero_choise()
            else:
                self.monster_antal_atack +=1
                self.hero_choise()

    def hero_choise(self):
        hero_choise_menu = '''Välj mellan följande:
                                1. Försöka atackera
                                2. Försöka fly\n'''
        hero_choice = input(hero_choise_menu)
        if hero_choice == '1':
            self.heroes_atack()
#        elif hero_choice == '2':
#            self.hero_tries_to_fly

#    def strid_loop(self):
#       while self.fighters > 1:

    def hero_tries_to_fly(self):
        pass

def main():
    foo = Strid()
    foo.huvud_menu()

if __name__ == '__main__':
    main()