import random


class Skatter:
    def __init__(self, värde, vanlighet):
        self.värde = värde
        self.vanlighet = vanlighet


class Lösa_slantar(Skatter):
    def __init__(self):
        super().__init__(2, 40)

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.4


class Pengapung(Skatter):
    def __init__(self):
        super().__init__(6, 20)

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.2


class Guldsmycket(Skatter):
    def __init__(self):
        super().__init__(10, 15)

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.15


class Ädelsten(Skatter):
    def __init__(self):
        super().__init__(14, 10)

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.1


class Liten_skattkista(Skatter):
    def __init__(self):
        super().__init__(20, 5)

    @classmethod
    def chance_of_appearance(cls):
        return random.random() <= 0.05
