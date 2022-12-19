# Single line comments cuz of pytest giving warnings when using multi-line comments.
# How to install & run;
# 1.  -   py -m venv .venv
# 1.1 -   .\.venv\Scripts\Activate.ps1
# 2.  -   pip install -r requirements.txt
# 2.1 -   pip install pytest-mock
# 3.  -   pytest tests/test_karaktärer.py


import pytest
import builtins

from karaktärer import Character, Riddaren, Trollkarlen, Tjuven


def test_character():
    # Skapar en random karaktär
    character = Character(10, 20, 15, 5)

    assert character.initiative == 10
    assert character.life == 20
    assert character.attack == 15
    assert character.agility == 5


def test_riddaren():
    riddaren = Riddaren()

    assert riddaren.initiative == 5
    assert riddaren.life == 9
    assert riddaren.attack == 6
    assert riddaren.agility == 4
    assert riddaren.name == "The Knight"
    assert riddaren.riddare_skill == "Sköldblock"
    assert riddaren.block_chans == True


def test_riddaren_use_skill():
    riddaren = Riddaren()

    assert riddaren.use_skill() == "Riddaren använder Sköldblock och blockar attacken."


def test_trollkarlen():
    trollkarlen = Trollkarlen()

    assert trollkarlen.initiative == 6
    assert trollkarlen.life == 4
    assert trollkarlen.attack == 9
    assert trollkarlen.agility == 5
    assert trollkarlen.name == "The Wizard"
    assert trollkarlen.trollkarl_skill == "Ljussken"


def test_trollkarlen_use_skill(mocker):
    # Använder 'mocker' från 'pytest' i detta test
    trollkarlen = Trollkarlen()

    # Simulerar random chansen från use_skill funktionen, i detta fall så ska den misslyckas
    mocker.patch('random.random', return_value=0.9)
    assert trollkarlen.use_skill() == "Trollkarlen använde Ljussken men misslyckas att fly!"

    # I detta fall så ska use_skull funktionen lyckas
    mocker.patch('random.random', return_value=0.5)
    assert trollkarlen.use_skill() == "Trollkarlen använde Ljussken och lyckades fly!"


def test_tjuven():
    tjuven = Tjuven()

    assert tjuven.initiative == 7
    assert tjuven.life == 5
    assert tjuven.attack == 5
    assert tjuven.agility == 7
    assert tjuven.name == "The Thief"
    assert tjuven.tjuv_skill == "Kritisk träff"


def test_tjuven_use_skill(mocker):
    tjuven = Tjuven()

    # Samma logik som för testen på Trollkarlen
    mocker.patch('random.random', return_value=0.5)
    assert tjuven.use_skill() == "Tjuven använde sin Kritisk träff men misslyckas att göra dubbel damage"

    mocker.patch('random.random', return_value=0.2)
    assert tjuven.use_skill() == "Tjuven använde sin Kritisk träff och lyckas göra dubbel damage"