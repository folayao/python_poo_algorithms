class Lavadora:
    """docstring for Lavadora."""

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_agua(temperatura)
        self._aniadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _aniadir_jabon(self):
        print(f'Añadiendo jabon')
        pass

    def _lavar(self):
        print(f'Lavando')
        pass

    def _centrifugar(self):
        print(f'Secando ropa ')
        pass


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
