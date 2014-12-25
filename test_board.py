
import board

def test_empty():
    brd = board.empty()
    assert len(brd) == 9*9
    for square in brd:
        assert square == 0
