import random


class Character:
    def __init__(self, initiative, life, attack, agility):
        self.initiative = initiative
        self.life = life
        self.attack = attack
        self.agility = agility


class Riddaren(Character):
    def __init__(self):
        super().__init__(5, 9, 6, 4)
        self.name = "The Knight"
        self.riddare_skill = "Shield block"
        self.block_chans = True

    def use_skill(self):
        return f"{self.name} used his {self.riddare_skill} and blocks the attack."


class Trollkarlen(Character):
    def __init__(self):
        super().__init__(6, 4, 9, 5)
        self.trollkarl_skill = "Shining light"
        self.name = "The Wizard"

    def use_skill(self):
        oddsen = random.random() <= 0.80
        if oddsen is True:
            return f"{self.name} used his {self.trollkarl_skill} and managed to escape!"
        elif oddsen is False:
            return f'{self.name} used his {self.trollkarl_skill} but fails to escape!'


class Tjuven(Character):
    def __init__(self):
        super().__init__(7, 5, 5, 7)
        self.tjuv_skill = "Critical hit"
        self.name = "The Thief"

    def use_skill(self):
        oddsen = random.random() <= 0.25
        if oddsen is True:
            return f'{self.name} used his {self.tjuv_skill} and manages to do double damage'
        elif oddsen is False:
            return f'{self.name} used his {self.tjuv_skill} but fails to deal double damage'


class Big_Spider(Character):
    def __init__(self):
        super().__init__(7, 1, 2, 3)
        self.name = "Big Spider"

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.2


class Skeleton(Character):
    def __init__(self):
        super().__init__(4, 2, 3, 3)
        self.name = "Skeleton"

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.15


class Orc(Character):
    def __init__(self):
        super().__init__(6, 3, 4, 4)
        self.name = "Orc"

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.1


class Troll(Character):
    def __init__(self):
        super().__init__(2, 4, 7, 2)
        self.name = "Troll"

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.05


def print_stats(character):
    print(f"Name: {character.name}")
    print(f"Initiative: {character.initiative}")
    print(f"Life: {character.life}")
    print(f"Attack: {character.attack}")
    print(f"Agility: {character.agility}\n")


def print_hero():
    print("")
    print_stats(character=Riddaren())
    print_stats(character=Trollkarlen())
    print_stats(character=Tjuven())
