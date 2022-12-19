from karta import Board
from meny import Menu
m = Menu()


def test_choice_of_hero():
    assert Menu.Choice_of_hero == """
    Choose your hero!
1. The Knight
2. The Wizard
3. The Thief
Type b or B to go back to the main menu"""


def test_main_menu_text():
    assert Menu.MAIN_MENU_TEXT == """
    Welcome!
1. Start a new game
2. Load game

Type q or Q to exit the program"""


def test_menu_commands():
    assert Menu.menu_commands(Menu, "5") is None


def test_submenu_exit():
    b = Board(4)
    assert b.subMenu_Exit() is None
    b = Board(5)
    assert b.subMenu_Exit() is None
    b = Board(8)
    assert b.subMenu_Exit() is None
