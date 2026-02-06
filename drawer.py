from chessboard import (
    Chessboard,
)
from figures import (
    Figure,
    Figure_type,
)
from utils import (
    ChessboardNumbers,
)
from const import (
    BOARD_HEIGHT,
    BOARD_WIDTH,
)


class Drawer:
    def __init__(self):
        pass

    def draw_chessboard(
            self,
            chessboard: Chessboard,
    ) -> None:
        print('  ', end=" | ")
        for l in range(BOARD_WIDTH):
            print(ChessboardNumbers(l).name, end=" | ")
        print("\n" + "------" * 6)

        for _line in range(BOARD_WIDTH):
            print(f' {ChessboardNumbers(_line).value + 1}', end=" | ")
            for cell in chessboard.board[_line].cells:
                cell_marker =  ' ' if cell.color.value else '#'
                
                _figure: Figure = cell.figure
                if _figure:
                    _figure_type: Figure_type = _figure.figure_type

                    if _figure_type == Figure_type.PAWN:
                        cell_marker = 'P'
                    if _figure_type == Figure_type.BISHOP:
                        cell_marker = 'B'
                    if _figure_type == Figure_type.ROOK:
                        cell_marker = 'R'
                    if _figure_type == Figure_type.QUEEN:
                        cell_marker = 'Q'
                    if _figure_type == Figure_type.KING:
                        cell_marker = 'K'
                    if _figure_type == Figure_type.KNIGHT:
                        cell_marker = 'N'

                if cell.ability:
                    cell_marker =  'A'
            
                print(cell_marker, end=" | ")
            print("\n" + "------" * 6)
        return