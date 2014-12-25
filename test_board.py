
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
