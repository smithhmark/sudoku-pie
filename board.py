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

def _index(col, row):
    # find the offset into a backing array from a position
    # index = rownum * rowlen + colnum
    if col >= HEIGHT or row >= WIDTH:
        ### should throw exception
        return -1
    if col < 0 or row < 0:
        ### should throw exception
        return -1
    return row * WIDTH + col

def row(brd, ii):
    # returns the contents of a row, id'd by <ii>
    # index = rownum * rowlen + colnum
    start_idx = _index(0, ii)
    return brd[start_idx:(start_idx + WIDTH)]

def column(brd,ii):
    # returns the contents of a column, id'd by <ii>
    # index = rownum * rowlen + colnum
    col = []
    for ri in range(HEIGHT):
        col.append(brd[_index(ii, ri)])
        #col.append(brd[ri * WIDTH + ii])
    return col

SQUARES = [
    [0,0,0,1,1,1,2,2,2,],
    [0,0,0,1,1,1,2,2,2,],
    [0,0,0,1,1,1,2,2,2,],
    [3,3,3,4,4,4,5,5,5,],
    [3,3,3,4,4,4,5,5,5,],
    [3,3,3,4,4,4,5,5,5,],
    [6,6,6,7,7,7,8,8,8,],
    [6,6,6,7,7,7,8,8,8,],
    [6,6,6,7,7,7,8,8,8,],
    ]

def get_square(columnid, rowid):
    return SQUARES[rowid][columnid]

def square(brd, ii):
    # returns the contents of a square specified by <ii>
    # squares are id'd by index, starting at 0 in the "upper left" corner, 
    # across then down, see SQUARES global.
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

def sets(col, row):
    # takes a coordinate and retures the ordinals for each of the sets that
    # intersects that coordinate
    # returns a dict holding the ordinals.
    res = {
        'row': None,
        'col': None,
        'sqr': None,
        }
    res['row'] = row
    res['col'] = col
    res['sqr'] = get_square(col, row)
    return res
