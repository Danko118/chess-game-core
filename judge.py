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


        if figure.figure_type == Figure_type.BISHOP:
                return self.check_bishop(
                    figure.cell.position,
                    figure.hasmove,
                    figure.color,
                    board,
                )
        
        if figure.figure_type == Figure_type.KING:
                return self.check_king(
                    figure.cell.position,
                    figure.hasmove,
                    figure.color,
                    board,
                )

        if figure.figure_type == Figure_type.QUEEN:
                return self.check_queen(
                    figure.cell.position,
                    figure.hasmove,
                    figure.color,
                    board,
                )

        return []
    

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
    

    def get_diagonal_moves(
            self,
            original_position: Position,
            color: Color,
            diagonals: List[tuple],
            width: int,
            height: int,
            board: Chessboard,
    ) -> List[Optional[Cell]]:
        result: List[Optional[Cell]] = []

        for dx, dy in diagonals:
            x = original_position.x
            y = original_position.y
            while True:
                x += dx
                y += dy
                if not (0 <= x < width and 0 <= y < height):
                    break
                cell = board.get_cell(Position(x, y))
                _figure = cell.get()
                if _figure:
                    if _figure.color != color:
                        result.append(cell)
                    break
                result.append(cell)
        
        return result
    

    def get_square_moves(
            self,
            original_position: Position,
            color: Color,
            width: int,
            height: int,
            board: Chessboard,
    ) -> List[Optional[Cell]]:
        result: List[Optional[Cell]] = []

        for dx in range(-1,2):
            for dy in range(-1,2):
                _dx = original_position.x + dx
                _dy = original_position.y + dy

                if not (0 <= _dx < width and 0 <= _dy < height):
                    continue

                _cell = board.get_cell(Position(_dx, _dy))

                if not _cell: continue
                
                _figure = _cell.get()

                if not _figure: 
                    result.append(_cell)
                    continue
                
                if _figure.color != color: result.append(_cell)
        
        return result



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

        avaliable_cells: List[Optional[Cell]] = self.get_diagonal_moves(
            figure_position,
            color,
            [(0, 1), (0, -1), (1, 0), (-1, 0)],
            BOARD_WIDTH,
            BOARD_HEIGHT,
            board,
        )

        return [_ for _ in avaliable_cells if _]
    

    def check_bishop(
            self,
            figure_position: Position,
            hasmove: bool,
            color: Color,
            board: Chessboard,
    ) -> List[Cell]:

        avaliable_cells: List[Optional[Cell]] = self.get_diagonal_moves(
            figure_position,
            color,
            [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            BOARD_WIDTH,
            BOARD_HEIGHT,
            board,
        )

        return [_ for _ in avaliable_cells if _]
    

    def check_king(
            self,
            figure_position: Position,
            hasmove: bool,
            color: Color,
            board: Chessboard,
    ) -> List[Cell]:
        
        avaliable_cells: List[Optional[Cell]] = self.get_square_moves(
            figure_position,
            color,
            BOARD_WIDTH,
            BOARD_HEIGHT,
            board,
        )

        return [_ for _ in avaliable_cells if _]
    

    def check_queen(
            self,
            figure_position: Position,
            hasmove: bool,
            color: Color,
            board: Chessboard,
    ) -> List[Cell]:
        
        avaliable_cells: List[Optional[Cell]] = []
        
        avaliable_cells += self.get_square_moves(
            figure_position,
            color,
            BOARD_WIDTH,
            BOARD_HEIGHT,
            board,
        )

        avaliable_cells += self.get_diagonal_moves(
            figure_position,
            color,
            [(0, 1), (0, -1), (1, 0), (-1, 0)],
            BOARD_WIDTH,
            BOARD_HEIGHT,
            board,
        )

        avaliable_cells += self.get_diagonal_moves(
            figure_position,
            color,
            [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            BOARD_WIDTH,
            BOARD_HEIGHT,
            board,
        )

        return [_ for _ in avaliable_cells if _]
