
import board

def test_empty():
    brd = board.empty()
    assert len(brd) == 9*9
    for square in brd:
        assert square == 0

def test_illegal():
    brd = board.illegal()

    print(brd)
    for ii in range(len(brd)):
        assert brd[ii] == ii

def test_row():
    ibrd = board.illegal()

    rrow = board.row(ibrd, 0)
    assert(rrow == [0,1,2,3,4,5,6,7,8])
    rrow = board.row(ibrd, 1)
    assert(rrow == [9,10,11,12,13,14,15,16,17])
    rrow = board.row(ibrd, 8)
    assert(rrow == [72,73,74,75,76,77,78,79,80])
