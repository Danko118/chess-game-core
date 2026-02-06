from chessboard import (
    Chessboard,
)
from drawer import (
    Drawer,
)
from secretary import (
    Secretary,
)
from judge import (
    Judge,
)


# разный трэш
drawer = Drawer()
some_board = Chessboard()
judge = Judge()
secretary = Secretary(some_board, judge)
secretary.start_up()
_pawn = secretary.get_figure_by_id(2)
if _pawn:
    secretary.check_figure_abilities(_pawn)
drawer.draw_chessboard(secretary.chessboard)