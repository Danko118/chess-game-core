class Observer:
    '''Наблюдатель
    Смотрит за всеми ходами и может сказать, что было
    '''
    def __init__(
        self,
    ):
        self.moves = 0

    def make_turn(self):
        self.moves += 1
