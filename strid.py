from random import randint
from karaktärer import Riddaren, Tjuven, Trollkarlen


class Strid:
    def __init__(self):

        self.monster = {'name': 'jättespindel', 'initiativ': 7,
                        'tålighet': 5, 'atack': 2, 'smidighet': 3}

        self.monster_förmågor = [i for i in self.monster.values()]

        self.heroes_kast = 0
        self.monsters_kast = 0

        self.monster_antal_atack = 0

        self.heroes_antal_kast = []
        self.monsters_antal_kast = []

        self.monster_liv = self.monster_förmågor[2]

    def strid_huvud_menu(self):
        huvud_meny = '''Du har hamnat i ett rum med monster, vilket leder till en strid. \nDet ska nu bestämmas vem som ska få börja först'''
        print(huvud_meny)


    def bestäm_turordning(self):
        self.strid_huvud_menu()
        x = randint(1, 2)
        while self.heroes_kast == self.monsters_kast:
            if x == 1:
                self.monster["tålighet"] = 5
                self.monster_liv = self.monster_förmågor[2]
                if self.monster_liv > 0:
                    for x in range(self.hero.initiativ):
                        self.hero_role_dice(self.heroes_kast)
                        self.heroes_antal_kast.append(self.heroes_kast)
                    self.heroes_kast = sum(self.heroes_antal_kast)
                    print(f'{self.hero.name} har slagit: {self.heroes_kast}')
                    self.heroes_antal_kast.clear()
                    for x in range(self.monster_förmågor[1]):
                        self.monster_role_dice(self.monsters_kast)
                        self.monsters_antal_kast.append(self.monsters_kast)
                    self.monsters_kast = sum(self.monsters_antal_kast)
                    print(f'Monster har slagit: {self.monsters_kast}')
                    self.monsters_antal_kast.clear()
                    if self.heroes_kast > self.monsters_kast:
                        self.hero_choise()
                    elif self.heroes_kast < self.monsters_kast:
                        self.monster_atack()
            else:
                break

    def hero_role_dice(self, heroes_kast):
        self.heroes_kast = randint(1, 6)
        print(f'Hero har slagit: {self.heroes_kast}')

    def monster_role_dice(self, monster_kast):
        self.monsters_kast = randint(1, 6)
        print(f'Monster har slagit: {self.monsters_kast}')

    # def check_monster(self):
    #    if self.monster == class Jättespindel:

    def hero_choose(self):
        choice2 = input("Enter your choice 1-3 or b/B: ")
    # if choice2 == "b" or choice2 == "B":
    #     self.start_loop()
        if choice2 == "1":
            self.hero = 'Riddaren'
        elif choice2 == "2":
            self.hero = 'Trollkarlen'
        elif choice2 == "3":
            self.hero = 'Tjuven'
        else:
            print("\nYou didn't enter a valid input, try again!")

    def check_hero(self):
        # self.hero = hero_choose()
        if self.hero == 'Riddaren':
            self.hero = Riddaren()
            # self.bestäm_turordning()
        elif self.hero == 'Tjuven':
            self.hero = Tjuven()
            # self.bestäm_turordning()
        elif self.hero == 'Trollkarlen':
            self.hero = Trollkarlen()
            # self.bestäm_turordning()

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
        for x in range(self.monster_förmågor[4]):
            self.monster_role_dice(self.monsters_kast)
            self.monsters_antal_kast.append(self.monsters_kast)
        self.monsters_kast = sum(self.monsters_antal_kast)
        self.monsters_antal_kast.clear()
        print(f'Monster: {self.monsters_kast}')

        if self.heroes_kast > self.monsters_kast:
            self.monster_liv = self.monster_liv - 1
            print(f'Monster har {self.monster_liv} liv kvar')
            if self.monster_liv <= 0:
                self.monster.clear()
                print('Jättespindel dog')
                self.heroes_kast = 0
                self.monsters_kast = 0
            else:
                self.monster_atack()
        else:
            self.monster_atack()

    def monster_atack(self):
        self.heros_liv = self.hero.tålighet
        print('Monster försöker attackera')
        print('Monster kastar tärningar')
        for x in range(self.monster_förmågor[3]):
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
                    self.heroes_kast = 0
                    self.monsters_kast = 0
                else:
                    self.hero_choise()
        elif self.monsters_kast < self.heroes_kast:
            if self.hero.name == 'Riddaren' and self.monster_antal_atack == 0:
                print('Riddaren använder sin speciella förmåga, attacken blockerad')
                self.monster_antal_atack += 1
                self.hero_choise()
            else:
                self.monster_antal_atack += 1
                self.hero_choise()

    def hero_choise(self):
        hero_choise_menu = '''Välj mellan följande:
                                1. Försöka atackera
                                2. Försöka fly\n'''
        hero_choice = input(hero_choise_menu)
        if hero_choice == '1':
            self.heroes_atack()
        # elif hero_choice == '2':
        #     self.hero_tries_to_fly

#    def strid_loop(self):
#       while self.fighters > 1:

    # def hero_tries_to_fly(self):
    #     procent = self.hero.smidighet * 10
    #     procent = procent/100
    #     return random.random() <= procent
    # if hero_tries_to_fly() is True:
    #     print(f'Hero har lyckats')
    # elif hero_tries_to_fly() is True:
    #     print(f'Hero har misslyckats')