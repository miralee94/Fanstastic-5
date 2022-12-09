class Menu:

    MAIN_MENU_TEXT = """
            Welcome!

    1. Start a new game
    2. Load game
    
    Type q or Q to exit the program
    """

    Choice_of_hero = """
        Choose your hero!

    1. The knight

    Type b or B to go back to the main menu
    """

    Choice_of_map = """
        Choose your map!
    
    1. 4x4

    Type b or B to go back to the main menu
    """

    def user_choice(self):
        return input("Enter your choice 1-2 or q/Q: ")

    def hero_choice(self):
        return input("Enter your choice 1 or b/B: ")

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
        print(Menu.Choice_of_hero)
        choice2 = self.hero_choice()
        self.wait_for_user
        print(Menu.Choice_of_map)
        choice3 = self.map_choice()

        

    def hero_menu_commands(self, choice2):
        if choice2 == "b" or choice2 == "B":
            Menu.start_loop
        elif choice2 == "1":
            pass
        else:
            print("\nYou didn't enter a valid input, try again!")


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