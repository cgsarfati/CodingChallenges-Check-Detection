"""Given a chessboard with one K and one Q, see if the K can attack the Q.

This function is given coordinates for the king and queen on a chessboard.
These coordinates are given as a letter A-H for the columns and 1-8 for the
row (see below for example):

Queens can move in any direction: horizontally, vertically, or diagonally,
as far as possible.

This function returns True if the king is in the line of attack of the queen.

For example, these boards show the king under attack:

8    . . . . . . . .      . . . . . . . .      . . . . . . . .    8
7    . . . . . . . .      . . . . . . . .      . K . . . . . .    7
6    . . . K . . . Q      . . . . K . . .      . . . . . . . .    6
5    . . . . . . . .      . . . . . . . .      . . . Q . . . .    5
4    . . . . . . . .      . . . . Q . . .      . . . . . . . .    4
3    . . . . . . . .      . . . . . . . .      . . . . . . . .    3
2    . . . . . . . .      . . . . . . . .      . . . . . . . .    2
1    . . . . . . . .      . . . . . . . .      . . . . . . . .    1
     A B C D E F G H      A B C D E F G H      A B C D E F G H

     K=D6, Q=H6           K=E6, Q=E4           K=B7, Q=D5

>>> check("D6", "H6")
True

>>> check("E6", "E4")
True

>>> check("B7", "D5")
True

>>> check("A1", "H8")
True

>>> check("A8", "H1")
True

>>> check("D6", "H7")
False

>>> check("E6", "F4")
False
"""


def col_to_num(col):
    """Turns A -> 1, B -> 2, etc."""

    return {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[col]


def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7":
    """

    # insights: attacked (True) if
        # vertical -- any 1-8 if same letter
        # horizontol -- any A-H if same #
        # diagonal -- diff b/w letter-to-letter and num-to-num is same
            # take into account diff. directions of diagonals (abs. value needed)

    # isolate row/col of K/Q
    king_col = col_to_num(king[0])
    king_row = int(king[1])
    queen_col = col_to_num(queen[0])
    queen_row = int(queen[1])

    # vertical/horizontal check
    if king_col == queen_col or king_row == queen_row:
        return True

    # diagonal check
    return abs(king_col - queen_col) == abs(king_row - queen_row)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT GAME!\n"
