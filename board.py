# board.py


HEIGHT = 9
WIDTH = 9
LENGTH = HEIGHT * WIDTH

def empty():
    return [0] * (HEIGHT * WIDTH)

def illegal():
    brd = empty()
    for idx, unused_sqr in enumerate(brd):
        brd[idx] = idx
    return brd

def row(brd, ii):
    # index = rownum * rowlen + colnum
    start_idx = ii * WIDTH
    return brd[start_idx:(start_idx + WIDTH)]

def column(row,ii):
    pass

def validate(brd):
    down = [set() for unused in range(9)]
    across = [set() for unused in range(9)]
    squares = [set() for unused in range(9)]


