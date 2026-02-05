from enum import Enum

class Position:
    def __init__(
            self,
            x: int,
            y: int,
    ):
        self.x = x
        self.y = y


    def __str__(
            self
    ) -> str:
        return f'({self.x}, {self.y})'


class Color(Enum):
    '''Логтка цвета.
    Чтобы запомнить если полностью включить пиксель (255),
    то его свет будет белым
    Отутсвие света - Тьма
    '''
    BLACK = 0
    WHITE = 1
