from chessboard import (
    Chessboard,
)
from drawer import (
    Drawer,
)
from secretary import (
    Secretary,
)


# разный трэш
drawer = Drawer()
some_board = Chessboard()
secretary = Secretary(some_board)
secretary.start_up()
drawer.draw_chessboard(secretary.board)