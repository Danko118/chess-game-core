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

        if figure.figure_type == Figure_type.PAWN:
            if _to_cell in self.check_pawn(
                figure.cell.position,
                figure.hasmove,
                board,
            ):
                return True

        return False


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
