class Skatter:
    def __init__(self,värde,vanlighet):
        self.värde = värde
        self.vanlighet = vanlighet


class Lösa_slantar(Skatter):
    super().__init__(2,40)

class Pengapung(Skatter):
    super().__init__(6,20)

class Guldsmycket(Skatter):
    super().__init__(10,15)

class Ädelsten(Skatter):
    super().__init__(14,10)

class Liten_skattkista(Skatter):
    super().__init__(20,5)
