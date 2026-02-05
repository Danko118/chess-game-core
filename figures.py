from typing import List
from utils import (
    Color,
    Position,
)


class Figure:
    def __init__(
            self,
            id: int,
            color: Color,
        ):
        self.id = id
        self.cell = None
        self.hasmove = False
        self.color = color


    def __str__(
            self,
    ) -> str:
        return f'Фигура: {self.get_marker()} \nID: {self.id} \nПозиция: {self.cell.position}'
    

    def get_marker(
              self,
    ) -> str:
         return 'F'


    def move_to(
            self,
            position: Position,
    ) -> None:
        self.cell.clear()
        self.hasmove = True
        _cell = self.board.get_cell(position)
        _cell.set(self)