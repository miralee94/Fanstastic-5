from karaktärer import print_hero, Riddaren, Tjuven, Trollkarlen
from battle_example_1 import Strid

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

    # Choice_of_map = """
    #     Choose your map!
    
    # 1. 4x4

    # Type b or B to go back to the main menu
    # """

    def user_choice(self):
        return input("Enter your choice 1-2 or q/Q: ")

    def hero_choice(self):
        return input("Enter your choice 1-3 or b/B: ")

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
            Menu.new_game(self)
        elif choice == "2":
            pass
            #ladda redan påbörjat spel funktion
        else:
            print("\nYou didn't enter a valid input, try again!")

    
    def new_game(self):
        player_name = self.name_choice()
        print_hero()
        print(Menu.Choice_of_hero)
        choice2 = self.hero_choice()
        self.hero_menu_commands(choice2)
        self.wait_for_user()
        self.strid_huvud_menu()
        s = Strid()
        s.bestäm_turordning()
        # print(Menu.Choice_of_map)
        # choice3 = self.map_choice()

    def strid_huvud_menu(self):
        huvud_meny = '''Du har hamnat i ett rum med monster, vilket leder till en strid. \nDet ska nu bestämmas vem som ska få börja först'''
        print(huvud_meny)


    def hero_menu_commands(self, choice2):
        if choice2 == "b" or choice2 == "B":
            Menu.start_loop(self)
        elif choice2 == "1":
            self.hero = Riddaren()
        elif choice2 == "2":
            self.hero = Trollkarlen()
        elif choice2 == "3":
            self.hero = Tjuven()
        else:
            print("\nYou didn't enter a valid input, try again!")


    def hero_2(self):
        return self.hero


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