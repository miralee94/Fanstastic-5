from random import randint, random
from karaktärer import Riddaren, Tjuven, Trollkarlen


class Strid:
    def __init__(self):

        self.monster = {'name': 'jättespindel', 'initiativ': 7,
                        'tålighet': 5, 'attack': 2, 'smidighet': 3}

        self.monster_abilitys = [i for i in self.monster.values()]

        # self.fighters = ['riddare', 'jättespindel']

        self.heroes_roll = 0
        self.monsters_roll = 0

        self.monster_total_attack = 0

        self.heroes_total_roll = []
        self.monsters_total_roll = []

        self.monster_life = self.monster_abilitys[2]

    def battle_main_menu(self):
        main_menu = '''You have ended up in a room with monsters, which leads to a battle. \nIt will now be decided who will get to start first\n'''
        print(main_menu)

    def turn_order(self, monster):
        self.battle_main_menu()
        while self.heroes_roll == self.monsters_roll:
            if self.monster_life > 0:
                for x in range(self.hero.initiative):
                    self.hero_role_dice(self.heroes_roll)
                    self.heroes_total_roll.append(self.heroes_roll)
                self.heroes_roll = sum(self.heroes_total_roll)
                print(f'{self.hero.name} total roll: {self.heroes_roll}\n')
                self.heroes_total_roll.clear()
                for x in range(self.monster_abilitys[1]):
                    self.monster_role_dice(self.monsters_roll)
                    self.monsters_total_roll.append(self.monsters_roll)
                self.monsters_roll = sum(self.monsters_total_roll)
                print(f'Monster total roll: {self.monsters_roll}\n')
                self.monsters_total_roll.clear()
                if self.heroes_roll > self.monsters_roll:
                    self.hero_choise()
                elif self.heroes_roll < self.monsters_roll:
                    self.monster_attack()
            else:
                break

    def hero_role_dice(self, heroes_roll):
        self.heroes_roll = randint(1, 6)
        print(f'{self.hero.name} roll: {self.heroes_roll}')

    def monster_role_dice(self, monster_roll):
        self.monsters_roll = randint(1, 6)
        print(f'Monster roll: {self.monsters_roll}')

    # def check_monster(self):
    #    if self.monster == class Jättespindel:

    def hero_choose(self):
        choice2 = input("Enter your choice 1-3: ")
        if choice2 == "1":
            self.hero = 'Riddaren'
        elif choice2 == "2":
            self.hero = 'Trollkarlen'
        elif choice2 == "3":
            self.hero = 'Tjuven'
        else:
            print("\nYou didn't enter a valid input, try again!")

    def check_hero(self):
        if self.hero == 'Riddaren':
            self.hero = Riddaren()
        elif self.hero == 'Tjuven':
            self.hero = Tjuven()
        elif self.hero == 'Trollkarlen':
            self.hero = Trollkarlen()

    def heroes_attack(self):
        print(f'{self.hero.name} tries to attack')
        print(f'{self.hero.name} Hero roll dice')
        for x in range(self.hero.attack):
            self.hero_role_dice(self.heroes_roll)
            self.heroes_total_roll.append(self.heroes_roll)
        self.heroes_roll = sum(self.heroes_total_roll)
        self.heroes_total_roll.clear()
        print(f'{self.hero.name} total roll: {self.heroes_roll}\n')

        print('Monster roll dice')
        for x in range(self.monster_abilitys[4]):
            self.monster_role_dice(self.monsters_roll)
            self.monsters_total_roll.append(self.monsters_roll)
        self.monsters_roll = sum(self.monsters_total_roll)
        self.monsters_total_roll.clear()
        print(f'Monster total roll: {self.monsters_roll}\n')

        if self.heroes_roll > self.monsters_roll:
            self.monster_life = self.monster_life - 1
            print(f'Monster has {self.monster_life} life left\n')
            if self.monster_life <= 0:
                self.monster.clear()
                print('Monster died')
                self.heroes_roll = 0
                self.monsters_roll = 0
            else:
                self.monster_attack()
        else:
            print(f'{self.hero.name} missed the attack')
            self.monster_attack()

    def monster_attack(self):
        self.heros_liv = self.hero.life
        print('Monster tries to attack')
        print('Monster roll dice')
        for x in range(self.monster_abilitys[3]):
            self.monster_role_dice(self.monsters_roll)
            self.monsters_total_roll.append(self.monsters_roll)
        self.monsters_roll = sum(self.monsters_total_roll)
        self.monsters_total_roll.clear()
        print(f'Monster total roll: {self.monsters_roll}\n')

        print(f'{self.hero.name} roll dice')
        for x in range(self.hero.agility):
            self.hero_role_dice(self.heroes_roll)
            self.heroes_total_roll.append(self.heroes_roll)
        self.heroes_roll = sum(self.heroes_total_roll)
        self.heroes_total_roll.clear()
        print(f'{self.hero.name} total roll: {self.heroes_roll}\n')

        if self.monsters_roll > self.heroes_roll:
            if self.hero.name == 'Riddaren' and self.monster_total_attack == 0:
                print(
                    'Riddaren använder sin speciella förmåga, attacken blockerad\n')
                self.monster_total_attack += 1
                self.hero_choise()
            else:
                self.hero.life = self.hero.life - 1
                print(f'{self.hero.name} has {self.hero.life} life left')
                if self.hero.life <= 0:
                    print(f'{self.hero.name} died')
                    print("Game over")
                    self.heroes_roll = 0
                    self.monsters_roll = 0
                else:
                    self.hero_choise()
        elif self.monsters_roll < self.heroes_roll:
            if self.hero.name == 'Riddaren' and self.monster_total_attack == 0:
                # print('Riddaren använder sin speciella förmåga, attacken blockerad\n')
                print("Monster missed the attack")
                self.monster_total_attack += 1
                self.hero_choise()
            else:
                print("Monster missed the attack")
                self.monster_total_attack += 1
                self.hero_choise()

    def hero_choise(self):
        hero_choise_menu = '''Choose the following:
1. Try to attack
2. Try to escape\n'''
        hero_choice = input(hero_choise_menu)
        if hero_choice == '1':
            self.heroes_attack()
        elif hero_choice == '2':
            self.hero_try_escape()
            if self.hero_try_escape() is True:
                print(f'{self.hero.name} escaped')
            elif self.hero_try_escape() is False:
                print(f'{self.hero.name} failed to escape')
                self.monster_attack()

    def hero_try_escape(self):
        procent = self.hero.agility * 10
        procent = procent/100
        return random() <= procent

# def main():
#     foo = Strid()
#     foo.huvud_menu()


# if __name__ == '__main__':
#     main()
