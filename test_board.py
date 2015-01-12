
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

def test_column():
    ibrd = board.illegal()
    rcol = board.column(ibrd, 0)
    ecol = [0,9,18,27,36,45,54,63,72]
    print("%s ?= %s" %(rcol, ecol))
    assert(rcol == [0,9,18,27,36,45,54,63,72])
    rcol = board.column(ibrd, 1)
    assert(rcol == [1,10,19,28,37,46,55,64,73])
    rcol = board.column(ibrd, 8)
    assert(rcol == [8,17,26,35,44,53,62,71,80])
