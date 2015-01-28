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

def column(brd,ii):
    # index = rownum * rowlen + colnum
    col = []
    for ri in range(HEIGHT):
        col.append(brd[ri * WIDTH + ii])
    return col

def square(brd, ii):
    # squares are id'd by index, starting at 0 in the "upper left" corner, 
    # across then down
    sqr = []
    if ii in [0,3,6]:
        colstart = 0
        colstop = 3
    elif ii in [1,4,7]:
        colstart = 3
        colstop = 6
    else:
        colstart = 6
        colstop = 9
    if ii in [0,1,2]:
        rowstart = 0
        rowstop = 3
    elif ii in [3,4,5]:
        rowstart = 3
        rowstop = 6
    else:
        rowstart = 6
        rowstop = 9
    print("c0: %s" % colstart)
    print("c1: %s" % colstop)
    print("r0: %s" % rowstart)
    print("r1: %s" % rowstop)
    for rid in range(rowstart, rowstop):
        sqr.extend(row(brd, rid)[colstart:colstop])
    return sqr

def validate(brd):
    down = [set() for unused in range(9)]
    across = [set() for unused in range(9)]
    squares = [set() for unused in range(9)]

def validate_set(data):
    # validate that a single row, column, or square is valid
    for xx in range(1,10):
        yy = data.count(xx)
        if yy not in [0,1]:
            return False
    for ii in data:
        if ii not in list(range(10)):
            return False
    if len(data) != 9:
        return False
    return True
