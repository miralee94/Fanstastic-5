import random


class Character:
    def __init__(self, initiativ, tålighet, attack, smidighet):
        self.initiativ = initiativ
        self.tålighet = tålighet
        self.attack = attack
        self.smidighet = smidighet


class Riddaren(Character):
    def __init__(self, initiativ, tålighet, attack, smidighet):
        super().__init__(initiativ, tålighet, attack, smidighet)
        self.riddare_skill = "Sköldblock"
        self.block_chans = True

    def use_skill(self):
        if self.block_chans:
            print(
                f"Riddaren använder {self.riddare_skill} och blockar attacken.")
            self.block_chans = False
        elif random.random() <= 0.50:
            print(
                f"Riddaren använder {self.riddare_skill} och blockar attacken.")
            self.block_chans = False
        else:
            print(
                f"Riddaren använder {self.riddare_skill} och misslyckas med att blockera attacken.")


class Trollkarlen(Character):
    def __init__(self, initiativ, tålighet, attack, smidighet):
        super().__init__(initiativ, tålighet, attack, smidighet)
        self.trollkarl_skill = "Ljussken"

    def use_skill(self):
        if random.random() <= 0.80:
            print(
                f"Trollkarlen använde {self.trollkarl_skill} och lyckades fly!")
            # Lägg till chans att fly funktion här? Indentera ett steg :)
        else:
            print(
                f"Trollkarlen använde {self.trollkarl_skill} men har misslyckats att fly!")


class Tjuven(Character):
    def __init__(self, initiativ, tålighet, attack, smidighet):
        super().__init__(initiativ, tålighet, attack, smidighet)
        self.tjuv_skill = "Kritisk träff"

    def use_skill(self):
        if random.random() <= 0.25:
            print(
                f"Tjuven försöker träffa en {self.tjuv_skill} och lyckas! Attacken gör dubbel mängd skada!")
        else:
            print(
                f"Tjuven försöker träffa en {self.tjuv_skill} men misslyckas och missar attacken.")


class big_spider(Character):
    def __init__(self):
        super().__init__(7, 1, 2, 3)
        self.name = "Big Spider"

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.2

class skeleton(Character):
    def __init__(self):
        super().__init__(4, 2, 3, 3)
        self.name = "Skeleton"

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.15

class orc(Character):
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

    
    


if __name__ == "__main__":
    # Exempel på hur man instanserar klassen
    riddare = Riddaren(initiativ=5, tålighet=9, attack=6, smidighet=4)
    # Exempel på hur man använder klassen, i detta fall Riddarens specialförmåga
    riddare.use_skill()