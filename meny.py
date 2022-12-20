from karaktärer import print_hero
from karta import Board


class Menu:

    MAIN_MENU_TEXT = """
    Welcome!
1. Start a new game
2. Load game (Not working)

Type q or Q to exit the program"""

    Choice_of_hero = """
    Choose your hero!
1. The Knight
2. The Wizard
3. The Thief
Type b or B to go back to the main menu"""

    def user_choice(self):
        return input("Enter your choice 1-2 or q/Q: ")

    def name_choice(self):
        return input("Please enter the player name: ")

    def menu_commands(self, choice):
        if choice == "q" or choice == "Q":
            self.running = False
        elif choice == "1":
            self.new_game()
        elif choice == "2":
            pass
            # ladda redan påbörjat spel funktion
        else:
            print("\nYou didn't enter a valid input, try again!")

    def new_game(self):
        b = Board(0)
        player_name = self.name_choice()
        print_hero()
        print(Menu.Choice_of_hero)
        b.hero_choose()
        b.check_hero()
        b.size_board()
        b.starting_pos()
        while True:
            b.moving_topos()

    def start_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_choice()
            self.menu_commands(choice)


def main():
    menu = Menu()
    menu.start_loop()


if __name__ == '__main__':
    main()
