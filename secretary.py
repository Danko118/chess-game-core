from chessboard import (
    Chessboard,
    Cell,
)
from figures import (
    Figure,
)
from utils import (
    Position,
    Color,
)

class Secretary:
    '''Секретарь.
    Сущность которая управляет доской
    итд
    '''
    def __init__(
            self,
            board: Chessboard,
    ):
        self.board = board


    def place_figure(
            self,
            figure: Figure,
            _position: Position
    ) -> bool:
        _cell = self.board.get_cell(_position)
        if not _cell.figure:
            _cell.set(figure)
            self.board.figures.append(figure)
            return True
        return False


    def start_up(self):
        figures = [
            (Figure(1,Color.WHITE), Position(2,3)),
        ]

        for figure in figures:
            self.place_figure(figure[0], figure[1])


    def move_figure(
            self,
            from_position: Position,
            to_position: Position,      
    ) -> bool:
        from_cell = self.board.get_cell(from_position)
        if from_cell.get() is None:
            return False
        
        to_cell = self.board.get_cell(to_position)
        if to_cell.get() is not None:
            return False
        
        from_cell.get().move_to(to_position)
        return True
