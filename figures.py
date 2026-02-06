from enum import Enum
from typing import List
from utils import (
    Color,
    Position,
)


class Figure_type(Enum):
    PAWN = 0
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    KING = 4
    QUEEN = 5


class Figure:
    def __init__(
            self,
            id: int,
            color: Color,
            figure_type: Figure_type,
        ):
        self.id = id
        self.cell = None
        self.hasmove = False
        self.color = color
        self.figure_type = figure_type


    def __str__(
            self,
    ) -> str:
        return f'Фигура: {self.get_marker()} \nID: {self.id} \nПозиция: {self.cell.position}'


    def move_to(
            self,
            position: Position,
    ) -> None:
        self.cell.clear()
        self.hasmove = True
        _cell = self.board.get_cell(position)
        _cell.set(self)
