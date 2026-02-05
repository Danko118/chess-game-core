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
        self.figure: Figure = None
        self.line = line
        self.position: Position = position
        self.color: Color = Color.WHITE if (self.position.x + self.position.y) & 1 else Color.BLACK
        self.ability: bool = False


    def __str__(
            self,
    ) -> str:
        return self.get_marker()


    def get_marker(
            self
    ) -> str:
        if self.figure:
            return self.figure.get_marker()
        if self.ability:
            return 'A'
        return ' ' if self.color.value else '#'


    def get(
            self
    ) -> Figure:
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
        self.cells: list[Cell] = [Cell(Position(i , line_number), self) for i in range(BOARD_WIDTH)] 


    def get_ids(
            self,
    ) -> Set[int]:
        return set(figure.get().id for figure in self.cells if figure.get())


    def set_cell(
            self,
            cell_position,
            figure
        ):
        self.cells[cell_position].set(figure)


    def get_cell(
            self,
            cell_position,
    ):
        return self.cells[cell_position]


class Chessboard:
    def __init__(
            self
    ):
        self.board = [Line(i, self) for i in range(BOARD_HEIGHT)]
        self.figures = []


    def get_figures(
            self,
    ) -> List[Figure]:
        return self.figures


    def get_cell(
            self,
            position: Position,
    ) -> Cell:
        return self.board[position.y].get_cell(position.x)


    def place_figure(
            self,
            figure: Figure,
            position: Position,
    ) -> None:
        figure.board = self
        self.figures.append(figure)
        _cell = self.get_cell(position)
        _cell.set(figure)


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


    def get_figure_by_id(
            self,
            figure_id: int,
    ) -> Optional[Figure]:
        for figure in self.figures:
            if figure.id == figure_id:
                return figure
        return None


    def move_figure(
            self,
            from_position: Position,
            to_position: Position,      
    ) -> None:
        from_cell = self.get_cell(from_position)
        if from_cell.get() is None:
            return
        
        to_cell = self.get_cell(to_position)
        if to_cell.get() is not None:
            return
        
        from_cell.get().move_to(to_position)


    def check_figure_abilities(
            self,
            figure: Figure,
    ) -> None:
        for line in self.board:
            for cell in line.cells:
                if figure.can_move(cell.position):
                    cell.ability = True


    def draw_chess_board(
            self,
    ) -> None:
        
        for line in self.board:
            for cell in line.cells:
                print(cell, end=" | ")
            print("\n" + "____" * 8)


# разный трэш
some_board = Chessboard()
some_board.draw_chess_board()
print()
print(some_board.get_figure_by_id(1))
some_board.select_figure(1)
