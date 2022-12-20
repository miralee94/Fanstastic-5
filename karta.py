from treasure import Lösa_slantar, Pengapung, Guldsmycket, Ädelsten, Liten_skattkista
from random import randint, random
from karaktärer import Riddaren, Tjuven, Trollkarlen, Big_Spider, Skeleton, Orc, Troll
import os
import time


class Board:
    def __init__(self, size):
        # Initialize the size of the board
        self.size = size
        # Initialize the board with empty cells
        self.cells = [['O' for i in range(self.size)]
                      for j in range(self.size)]
        self.coord_x = 0
        self.coord_y = 0
        self.points = 0

        self.heroes_roll = 0
        self.monsters_roll = 0

        self.monster_träff = 0

        self.heroes_total_roll = []
        self.monsters_total_roll = []

        self.where_now = []
        self.besökta_rum = []

    def __str__(self):
        # This method is called when the object is printed,
        # e.g. print(my_board)
        # Create a string representation of the board
        board_str = ''
        for row in self.cells:
            # Add each cell and a space to the string
            board_str += ' '.join(row) + '\n'
        # Return the string
        return board_str

    def wait_for_user(self):
        input("\nPlease press ENTER to continue.\n")

    def set_cell(self, row, col, value):
        # Set the value of the cell at the given row and column
        self.cells[row][col] = value

    def size_board(self):
        while True:
            size = input("Choose your size of the map, 4, 5 or 8\n")
            if size == "4":
                self.my_board = Board(4)
                print(self.my_board)
                break
            elif size == "5":
                self.my_board = Board(5)
                print(self.my_board)
                break
            elif size == "8":
                self.my_board = Board(8)
                print(self.my_board)
                break
            else:
                print("Try again!")

    def starting_pos(self):
        while True:
            pos = input("""Wich corner would you like to start?
1. Left uppercorner
2. Right uppercorner
3. Left bottom corner
4. Right bottom corner\n""")
            if pos == "1":
                self.my_board.set_cell(0, 0, "H")
                os.system('cls')
                break
            elif pos == "2":
                self.my_board.set_cell(0, self.size - 1, "H")
                os.system('cls')
                break
            elif pos == "3":
                self.my_board.set_cell(self.size - 1, 0, "H")
                os.system('cls')
                break
            elif pos == "4":
                self.my_board.set_cell(self.size - 1, self.size - 1, "H")
                os.system('cls')
                break
            else:
                print("Try again!")

    def vart_är_jag(self):
        for j in self.my_board.cells:
            for i in j:
                if i == 'H':
                    self.coord_x = self.my_board.cells.index(j)
                    self.coord_y = j.index(i)
                    self.where_now.append(self.coord_x)
                    self.where_now.append(self.coord_y)

    def moving_topos(self):
        self.vart_är_jag()
        print(self.my_board)
        move = input("""\n
Enter Direction:
1. Left
2. Right
3. Up
4. Down \n""")
        try:
            if move == "1":
                self.my_board.set_cell(
                    (self.coord_x), self.coord_y, "X")
                self.besökta_rum.append(self.coord_x)
                self.besökta_rum.append(self.coord_y)
                self.my_board.set_cell(
                    self.coord_x, (self.coord_y - 1), 'H')
                print(self.my_board)
                self.create_a_room()
                self.moving_topos()
            elif move == "2":
                self.my_board.set_cell(
                    (self.coord_x), self.coord_y, "X")
                self.besökta_rum.append(self.coord_x)
                self.besökta_rum.append(self.coord_y)
                self.my_board.set_cell(
                    self.coord_x, (self.coord_y + 1), 'H')
                print(self.my_board)
                self.create_a_room()
                self.moving_topos()
            elif move == "3":
                self.my_board.set_cell(
                    (self.coord_x), self.coord_y, "X")
                self.besökta_rum.append(self.coord_x)
                self.besökta_rum.append(self.coord_y)
                self.my_board.set_cell(
                    (self.coord_x - 1), self.coord_y, 'H')
                print(self.my_board)
                self.create_a_room()
                self.moving_topos()
            elif move == "4":
                self.my_board.set_cell(
                    (self.coord_x), self.coord_y, "X")
                self.besökta_rum.append(self.coord_x)
                self.besökta_rum.append(self.coord_y)
                self.my_board.set_cell(
                    (self.coord_x + 1), self.coord_y, 'H')
                print(self.my_board)
                self.create_a_room()
                self.moving_topos()
            else:
                print("Try again!")
        except IndexError:
            self.subMenu_Exit()
            self.subMenu_Exit_choices()

    def subMenu_Exit(self):
        SUB_MENU_TEXT = """
You have gone outside the map...
1. Do you want to keep playing?
2. Do you want to exit?"""
        print(SUB_MENU_TEXT)

    def subMenu_Exit_choices(self):
        subMenuChoice = int(input("Select an option: "))
        if subMenuChoice == 1:
            self.go_back()
        elif subMenuChoice == 2:
            exit()  # Koppla Charalampos spara funktion
        else:
            print("You did not select a valid option, try again.")

    def create_a_room(self):
        self.shuffle_monster()
        self.shuffle_treasure()

    def shuffle_treasure(self):
        slantar = Lösa_slantar()
        slantar.chance_of_appearance()
        if slantar.chance_of_appearance() is True:
            self.treasure = slantar.value
            print(f'You found Lösa Slantar that is worth: {slantar.value}')
            self.points = self.points + slantar.value
            print(f'You have total of points: {self.points}')
        else:
            pass

        pengapung = Pengapung()
        pengapung.chance_of_appearance()
        if pengapung.chance_of_appearance() is True:
            self.treasure = slantar.value
            print(f'You found Pengapung that is worth: {pengapung.value}')
            self.points = self.points + pengapung.value
            print(f'You have total of points: {self.points}')
        else:
            pass

        guldsmycket = Guldsmycket()
        guldsmycket.chance_of_appearance()
        if guldsmycket.chance_of_appearance() is True:
            self.treasure = slantar.value
            print(f'You found Guldsmycke that is worth: {guldsmycket.value}')
            self.points = self.points + guldsmycket.value
            print(f'You have total of points: {self.points}')
        else:
            pass

        ädelsten = Ädelsten()
        ädelsten.chance_of_appearance()
        if ädelsten.chance_of_appearance() is True:
            self.treasure = slantar.value
            print(f'You found Ädelsten that is worth: {ädelsten.value}')
            self.points = self.points + ädelsten.value
            print(f'You have total of points: {self.points}')
        else:
            pass

        liten_kista = Liten_skattkista()
        liten_kista.chance_of_appearance()
        if liten_kista.chance_of_appearance() is True:
            self.treasure = slantar.value
            print(
                f'You found Liten skattkista that is worth: {liten_kista.value}')
            self.points = self.points + liten_kista.value
            print(f'You have total of points: {self.points}')
        else:
            pass

    def shuffle_monster(self):
        spider = Big_Spider()
        spider.chance_of_appearance()
        if spider.chance_of_appearance() is True:
            self.monster = Big_Spider()
            self.turn_order()
        else:
            pass

        skeleton = Skeleton()
        skeleton.chance_of_appearance()
        if skeleton.chance_of_appearance() is True:
            self.monster = Skeleton()
            self.turn_order()
        else:
            pass

        troll = Troll()
        troll.chance_of_appearance()
        if troll.chance_of_appearance() is True:
            self.monster = Troll()
            self.turn_order()
        else:
            pass

        orc = Orc()
        orc.chance_of_appearance()
        if orc.chance_of_appearance() is True:
            self.monster = Orc()
            self.turn_order()
        else:
            pass

    def battle_main_menu(self):
        main_menu = '''You have ended up in a room with monsters, which leads to a battle. \nIt will now be decided who will get to start first\n'''
        print(main_menu)

    def turn_order(self):
        self.battle_main_menu()
        self.wait_for_user()
        while self.heroes_roll == self.monsters_roll:
            if self.monster.life > 0:
                for x in range(self.hero.initiative):
                    self.hero_role_dice(self.heroes_roll)
                    self.heroes_total_roll.append(self.heroes_roll)
                self.heroes_roll = sum(self.heroes_total_roll)
                print(f'{self.hero.name} total roll: {self.heroes_roll}\n')
                self.wait_for_user()
                self.heroes_total_roll.clear()
                for x in range(self.monster.initiative):
                    self.monster_role_dice(self.monsters_roll)
                    self.monsters_total_roll.append(self.monsters_roll)
                self.monsters_roll = sum(self.monsters_total_roll)
                print(f'{self.monster.name} total roll: {self.monsters_roll}\n')
                self.wait_for_user()
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
        print(f'{self.monster.name} roll: {self.monsters_roll}')

    def hero_choose(self):
        while True:
            choice2 = input("Enter your choice 1-3: ")
            if choice2 == "1":
                self.hero = 'Riddaren'
                break
            elif choice2 == "2":
                self.hero = 'Trollkarlen'
                break
            elif choice2 == "3":
                self.hero = 'Tjuven'
                break
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

        print(f'{self.monster.name} roll dice')
        for x in range(self.monster.agility):
            self.monster_role_dice(self.monsters_roll)
            self.monsters_total_roll.append(self.monsters_roll)
        self.monsters_roll = sum(self.monsters_total_roll)
        self.monsters_total_roll.clear()
        print(f'{self.monster.name} total roll: {self.monsters_roll}\n')

        if self.heroes_roll > self.monsters_roll:
            if self.hero.name == 'The Thief':
                skill = self.hero.use_skill()
                print(skill)
                if skill == f'{self.hero.name} used his {self.hero.tjuv_skill} and manages to do double damage':
                    self.monster.life = self.monster.life - 1
            print(f'{self.hero.name} attacks')
            self.monster.life = self.monster.life - 1
            print(f'{self.monster.name} has {self.monster.life} life left\n')
            if self.monster.life <= 0:
                print(f'{self.monster.name} died\n')
                self.wait_for_user()
                os.system('cls')
                self.heroes_roll = 0
                self.monsters_roll = 0
                self.monster_träff = 0
            else:
                self.monster_attack()
        else:
            print(f'{self.hero.name} missed the attack\n')
            self.wait_for_user()
            self.monster_attack()

    def monster_attack(self):
        self.heros_liv = self.hero.life
        print(f'{self.monster.name} tries to attack')
        print(f'{self.monster.name} roll dice')
        for x in range(self.monster.attack):
            self.monster_role_dice(self.monsters_roll)
            self.monsters_total_roll.append(self.monsters_roll)
        self.monsters_roll = sum(self.monsters_total_roll)
        self.monsters_total_roll.clear()
        print(f'{self.monster.name} total roll: {self.monsters_roll}\n')

        print(f'{self.hero.name} roll dice')
        for x in range(self.hero.agility):
            self.hero_role_dice(self.heroes_roll)
            self.heroes_total_roll.append(self.heroes_roll)
        self.heroes_roll = sum(self.heroes_total_roll)
        self.heroes_total_roll.clear()
        print(f'{self.hero.name} total roll: {self.heroes_roll}\n')

        if self.monsters_roll > self.heroes_roll:
            if self.hero.name == 'The Knight' and self.monster_träff == 0:
                print(self.hero.use_skill())
                self.monster_träff = self.monster_träff + 1
                self.hero_choise()
            else:
                print(f'{self.monster.name} attacks')
                self.hero.life = self.hero.life - 1
                print(f'{self.hero.name} has {self.hero.life} life left')
                self.wait_for_user()
                if self.hero.life <= 0:
                    print(f'{self.hero.name} died')
                    print("Game over")
                    self.heroes_roll = 0
                    self.monsters_roll = 0
                    time.sleep(2)
                    exit()
                else:
                    self.hero_choise()
        elif self.monsters_roll < self.heroes_roll:
            print(f"{self.monster.name} missed the attack\n")
            self.hero_choise()

    def hero_choise(self):
        while True:
            hero_choise_menu = '''Choose the following:
1. Try to attack
2. Try to escape\n'''
            hero_choice = input(hero_choise_menu)
            if hero_choice == '1':
                self.heroes_attack()
                break
            elif hero_choice == '2':
                if self.hero.name == 'The Wizard':
                    skill = self.hero.use_skill()
                    print(skill)
                    if skill == f"{self.hero.name} used his {self.hero.trollkarl_skill} and managed to escape!":
                        self.heroes_roll = 0
                        self.monsters_roll = 0
                        self.go_back()
                    else:
                        self.monster_attack()
                        break
                elif self.hero_try_escape() is True:
                    self.heroes_roll = 0
                    self.monsters_roll = 0
                    print(f'{self.hero.name} escaped')
                    self.go_back()
                    break
                else:
                    print(f'{self.hero.name} failed to escape')
                    self.monster_attack()
                    break
            else:
                print("Try again!")

    def go_back(self):
        self.vart_är_jag()
        i = self.where_now[-1]
        j = self.where_now[-2]
        x = self.besökta_rum[-1]
        y = self.besökta_rum[-2]
        self.my_board.set_cell(j, i, 'X')
        self.my_board.set_cell(y, x, 'H')
        print(self.my_board)
        self.moving_topos()

    def hero_try_escape(self):
        procent = self.hero.agility * 10
        procent = procent/100
        return random() <= procent
