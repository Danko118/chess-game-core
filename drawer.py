from chessboard import (
    Chessboard,
    Line,
    Cell,
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
                
                if cell.figure:
                    cell_marker =  cell.figure.get_marker()

                if cell.ability:
                    cell_marker =  'A'
            
                print(cell_marker, end=" | ")
            print("\n" + "------" * 6)
        return