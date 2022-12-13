from karaktärer import print_hero
from strid import Strid
from karta import Board


class Menu:

    MAIN_MENU_TEXT = """
            Welcome!
    1. Start a new game
    2. Load game
    Type q or Q to exit the program
    """

    Choice_of_hero = """
        Choose your hero!
    1. The Knight
    2. The Wizard
    3. The Thief
    Type b or B to go back to the main menu
    """

    def user_choice(self):
        return input("Enter your choice 1-2 or q/Q: ")

    # def hero_choice(self):
    #     return input("Enter your choice 1-3 or b/B: ")

    def map_choice(self):
        return input("Enter your choice 1 or b/B: ")

    def name_choice(self):
        return input("Please enter the player name: ")

    def wait_for_user(self):
        if self.running:
            input("\nPlease press any key to continue.")

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

    # def starta_karta(self):
    #     b = Board(0)
    #     b.size_board()
    #     b.starting_pos()
    #     # b.moving_topos()


    def new_game(self):
        s = Strid()
        b = Board(0)
        player_name = self.name_choice()
        print_hero()
        print(Menu.Choice_of_hero)
        s.hero_choose()
        s.check_hero()
        self.wait_for_user()
        b.size_board()
        b.starting_pos()
        while True:
            b.moving_topos()
            s.bestäm_turordning()
            # self.cont_game()

    # def cont_game(self):
    #     Board.moving_topos(self)

    # def hero_menu_commands(self):
    #     choice2 = input("Enter your choice 1-3 or b/B: ")
    #     if choice2 == "b" or choice2 == "B":
    #         self.start_loop()
    #     elif choice2 == "1":
    #         self.hero = Riddaren()
    #     elif choice2 == "2":
    #         self.hero = Trollkarlen()
    #     elif choice2 == "3":
    #         self.hero = Tjuven()
    #     else:
    #         print("\nYou didn't enter a valid input, try again!")

    # def hero_choosed(self):
    #     return self.hero


    def start_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_choice()
            self.menu_commands(choice)
            self.wait_for_user()


def main():
    menu = Menu()
    menu.start_loop()


if __name__ == '__main__':
    main()