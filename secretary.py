from typing import Optional
from chessboard import (
    Chessboard,
    Cell,
)
from figures import (
    Figure,
    Figure_type,
)
from utils import (
    Position,
    Color,
)
from judge import (
    Judge,
)
from const import (
    BOARD_HEIGHT,
    BOARD_WIDTH,
)

class Secretary:
    '''Секретарь.
    Сущность которая управляет доской
    итд
    '''
    def __init__(
            self,
            chessboard: Chessboard,
            judge: Judge,
    ):
        self.chessboard = chessboard
        self.judge = judge
    

    def get_figure_by_id(
            self,
            figure_id: int,
    ) -> Optional[Figure]:
        for figure in self.chessboard.figures:
            if figure.id == figure_id:
                return figure
        return None
    

    def check_position(
            self,
            position: Position,
    ) -> bool:
        
        if not (0 <= position.x < BOARD_WIDTH):
            return False
        
        if not (0 <= position.y < BOARD_WIDTH):
            return False
        
        return True


    def place_figure(
            self,
            figure: Figure,
            _position: Position,
    ) -> bool:
        if not self.check_position(_position):
            return False

        _cell = self.chessboard.get_cell(_position)
        if not _cell.figure:
            _cell.set(figure)
            self.chessboard.figures.append(figure)
            return True
        return False


    def start_up(self):
        figures = [
            (
                Figure(
                    1,
                    Color.WHITE,
                    Figure_type.PAWN,
                ),
                Position(2,1),
            ),
            (
                Figure(
                    2,
                    Color.WHITE,
                    Figure_type.PAWN,
                ),
                Position(3,1),
            ),
        ]

        for figure in figures:
            self.place_figure(figure[0], figure[1])


    def move_figure(
            self,
            from_position: Position,
            to_position: Position,      
    ) -> bool:
        if not self.check_position(from_position):
            return False

        from_cell = self.chessboard.get_cell(from_position)
        if from_cell.get() is None:
            return False
        
        if not self.check_position(to_position):
            return False
        
        to_cell = self.chessboard.get_cell(to_position)
        if to_cell.get() is not None:
            return False
        
        _figure = from_cell.get()
        if not self.judge.check_move(
            self.chessboard,
            _figure,
            to_cell,
        ):
            return False
        
        _figure.move_to(to_position)
        return True


    def clear_board(
            self,     
    ) -> bool:
        for lines in self.chessboard.board:
            for cell in lines.cells:
                cell.clear()
        
        self.chessboard.figures = []
        return True
    

    def check_figure_abilities(
            self,
            figure: Figure,
    ) -> None:
        _cells = self.judge.get_all_figure_moves(
            self.chessboard,
            figure,
        )

        for cell in _cells:
            cell.ability = True
    

    def clear_abilites_mode(
            self,     
    ) -> bool:
        for lines in self.chessboard.board:
            for cell in lines.cells:
                cell.ability = False
        
        return True
