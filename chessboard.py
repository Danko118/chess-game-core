from typing import List, Set, Optional
from const import (
    BOARD_HEIGHT,
    BOARD_WIDTH,
)
from figures import (
    Figure,
)
from utils import (
    Color,
    Position,
)

class Cell:
    def __init__(
            self,
            position: Position,
            line,
    ):
        self.figure: Optional[Figure] = None
        self.line = line
        self.position: Position = position
        self.color: Color = Color.WHITE if (self.position.x + self.position.y) & 1 else Color.BLACK
        self.ability: bool = False


    def __str__(
            self,
    ) -> str:
        return self.get_marker()


    def get(
            self
    ) -> Optional[Figure]:
        return self.figure


    def set(
            self,
            _figure,
    ) -> None:
        self.figure = _figure
        _figure.cell = self


    def clear(
            self,
    ) -> None:
        self.figure = None


class Line:
    def __init__(
            self,
            line_number: int,
            board,
    ):
        self.line_number = line_number
        self.board = board
        self.cells: list[Cell] = [Cell(Position(i, line_number), self) for i in range(BOARD_WIDTH)] 


    def get_ids(
            self,
    ) -> Set[int]:
        return set(figure.get().id for figure in self.cells if figure.get())


    def set_cell(
            self,
            cell_position,
            figure
    ) -> None:
        self.cells[cell_position].set(figure)


    def get_cell(
            self,
            cell_position,
    ) -> Optional[Cell]:
        if cell_position < len(self.cells):
            return self.cells[cell_position]
        return None


class Chessboard:
    def __init__(
            self
    ):
        self.board = [Line(i, self) for i in range(BOARD_HEIGHT)]
        self.figures: List[Figure] = []


    def get_figures(
            self,
    ) -> List[Figure]:
        return self.figures


    def get_cell(
            self,
            position: Position,
    ) -> Optional[Cell]:
        return self.board[position.y].get_cell(position.x)


    def select_figure(
            self,
            figure_id: int,
    ) -> None:
        _figure = self.get_figure_by_id(figure_id)
        if not _figure:
            return
        
        self.check_figure_abilities(_figure)
        self.draw_chess_board()

        for line in self.board:
            for cell in line.cells:
                cell.ability = False


    def check_figure_abilities(
            self,
            figure: Figure,
    ) -> None:
        for line in self.board:
            for cell in line.cells:
                if figure.can_move(cell.position):
                    cell.ability = True
