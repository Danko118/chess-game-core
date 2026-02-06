from typing import List, Optional
from figures import (
    Figure,
    Figure_type,
)
from utils import (
    Position,
    Color,
)
from chessboard import (
    Cell,
    Chessboard,
)
from const import (
    BOARD_WIDTH,
    BOARD_HEIGHT,
)


class Judge:
    '''Сущность судьи
    (посмотрим насколько нужная сущность)
    должен диктовать правила
    '''

    def __init__(
            self,
    ):
        pass

    def check_move(
            self,
            board: Chessboard,
            figure: Figure,
            _to_cell: Cell,
    ) -> bool:

        _cells = self.get_all_figure_moves(
            board,
            figure,
        )

        return _to_cell in _cells


    def get_all_figure_moves(
            self,
            board: Chessboard,
            figure: Figure,
    ) -> List[Cell]:

        if figure.figure_type == Figure_type.PAWN:
                return self.check_pawn(
                    figure.cell.position,
                    figure.hasmove,
                    figure.color,
                    board,
                )
        

        if figure.figure_type == Figure_type.ROOK:
                return self.check_rook(
                    figure.cell.position,
                    figure.hasmove,
                    figure.color,
                    board,
                )

        return False
    

    def check_cell(
            self,
            cell: Optional[Cell],
            has_to_eat: bool,
            color: Color,
    ) -> Optional[Cell]:
        if not cell:
            return None
        
        if not cell.figure:
            if has_to_eat:
                return None
            return cell
        
        if has_to_eat and cell.figure.color != color:
            return cell
        
        return None


    def check_pawn(
            self,
            figure_position: Position,
            hasmove: bool,
            color: Color,
            board: Chessboard,
    ) -> List[Cell]:
        avaliable_cells: List[Optional[Cell]] = []
        
        _tmp_pos = Position(
                        figure_position.x,
                        figure_position.y + 1,
                    ) if color.value else Position(
                        figure_position.x,
                        figure_position.y - 1,
                    )
        avaliable_cells.append(
            self.check_cell(
                board.get_cell(_tmp_pos),
                False,
                color,
            )
        )
        
        if not hasmove and avaliable_cells[0]:
            _tmp_pos = Position(
                        figure_position.x,
                        figure_position.y + 2,
                    ) if color.value else Position(
                        figure_position.x,
                        figure_position.y - 2,
                    )
            avaliable_cells.append(
                self.check_cell(
                    board.get_cell(_tmp_pos),
                    False,
                    color,
                )
            )

        _tmp_pos = Position(
                        figure_position.x + 1,
                        figure_position.y + 1,
                    ) if color.value else Position(
                        figure_position.x + 1,
                        figure_position.y - 1,
                    )
        avaliable_cells.append(
            self.check_cell(
                board.get_cell(_tmp_pos),
                True,
                color,
            )
        )

        _tmp_pos = Position(
                        figure_position.x - 1,
                        figure_position.y + 1,
                    ) if color.value else Position(
                        figure_position.x - 1,
                        figure_position.y - 1,
                    )
        avaliable_cells.append(
            self.check_cell(
                board.get_cell(_tmp_pos),
                True,
                color,
            )
        )
        

        return [_ for _ in avaliable_cells if _]


    def check_rook(
            self,
            figure_position: Position,
            hasmove: bool,
            color: Color,
            board: Chessboard,
    ) -> List[Cell]:
        avaliable_cells: List[Optional[Cell]] = []

        for _cell_pos in range(figure_position.y + 1, BOARD_HEIGHT):
            _cell = board.get_cell(
                Position(
                    figure_position.x,
                    _cell_pos,
                )
            )
            _figure = _cell.get()

            if _figure and _figure.color != color:
                avaliable_cells.append(_cell)
            
            if not _figure:
                avaliable_cells.append(_cell)
            else:
                break
        
        for _cell_pos in range(figure_position.y - 1, -1, -1):
            _cell = board.get_cell(
                Position(
                    figure_position.x,
                    _cell_pos,
                )
            )
            _figure = _cell.get()

            if _figure and _figure.color != color:
                avaliable_cells.append(_cell)
            
            if not _figure:
                avaliable_cells.append(_cell)
            else:
                break
        
        for _cell_pos in range(figure_position.x + 1, BOARD_WIDTH):
            _cell = board.get_cell(
                Position(
                    _cell_pos,
                    figure_position.y,
                )
            )
            _figure = _cell.get()

            if _figure and _figure.color != color:
                avaliable_cells.append(_cell)
            
            if not _figure:
                avaliable_cells.append(_cell)
            else:
                break
        
        for _cell_pos in range(figure_position.x -1, -1, -1):
            _cell = board.get_cell(
                Position(
                    _cell_pos,
                    figure_position.y,
                )
            )
            _figure = _cell.get()

            if _figure and _figure.color != color:
                avaliable_cells.append(_cell)
            
            if not _figure:
                avaliable_cells.append(_cell)
            else:
                break

        

        return [_ for _ in avaliable_cells if _]
