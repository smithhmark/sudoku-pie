
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

def test_square():
    ibrd = board.illegal()
    rsqr = board.square(ibrd, 0)
    esqr = [0,1,2,9,10,11,18,19,20]
    print("%s ?= %s" %(rsqr, esqr))
    assert(rsqr == esqr)
    print("yes")

    rsqr = board.square(ibrd, 1)
    esqr = [3,4,5,12,13,14,21,22,23]
    print("%s ?= %s" %(rsqr, esqr))
    assert(rsqr == esqr)
    print("yes")

    rsqr = board.square(ibrd, 3)
    esqr = [27,28,29,36,37,38,45,46,47]
    print("%s ?= %s" %(rsqr, esqr))
    assert(rsqr == esqr)
    print("yes")


def test_validate_set():
    row = [1,2,3,4,5,6,7,8,9]
    assert board.validate_set(row)

    row = [0,0,0,4,0,0,0,0,0]
    assert board.validate_set(row)

    row = [0,0,0,4,0,4,0,0,0]
    assert not board.validate_set(row)

def test_get_square():
    rr, cc = 0, 0
    sqr = board.get_square(cc, rr)
    assert sqr == 0

    rr, cc = 3, 3
    sqr = board.get_square(cc, rr)
    assert sqr == 4

    rr, cc = 0, 3
    sqr = board.get_square(cc, rr)
    assert sqr == 1

    rr, cc = 3, 0
    sqr = board.get_square(cc, rr)
    print(sqr)
    assert sqr == 3

def test__index():
    tmp_brd = board.illegal()
    print(tmp_brd[-9:])
    assert board._index(0,0) == 0
    assert board._index(0,1) == 9
    assert board._index(1,0) == 1
    assert board._index(1,1) == 10
    assert board._index(8,8) == 80
    assert board._index(9,9) == -1
    assert board._index(-1,0) == -1
    assert board._index(0,-1) == -1

def test_sets():
    ret = board.sets(0,0)
    assert ret['row'] == 0
    assert ret['col'] == 0
    assert ret['sqr'] == 0

    ret = board.sets(1,0)
    print(ret)
    assert ret['row'] == 0
    assert ret['col'] == 1
    assert ret['sqr'] == 0

    ret = board.sets(0,1)
    print(ret)
    assert ret['row'] == 1
    assert ret['col'] == 0
    assert ret['sqr'] == 0

    ret = board.sets(3,3)
    print(ret)
    assert ret['row'] == 3
    assert ret['col'] == 3
    assert ret['sqr'] == 4

    ret = board.sets(3,0)
    print(ret)
    assert ret['row'] == 0
    assert ret['col'] == 3
    assert ret['sqr'] == 1

    ret = board.sets(8,8)
    print(ret)
    assert ret['row'] == 8
    assert ret['col'] == 8
    assert ret['sqr'] == 8

def test_from_string():
    in_put = """012345678
                012345678
                012345678
                012345678
                012345678
                012345678
                012345678
                012345678
                012345678"""
    expected_out_put = [
            [0,1,2,3,4,5,6,7,8,],
            [0,1,2,3,4,5,6,7,8,],
            [0,1,2,3,4,5,6,7,8,],
            [0,1,2,3,4,5,6,7,8,],
            [0,1,2,3,4,5,6,7,8,],
            [0,1,2,3,4,5,6,7,8,],
            [0,1,2,3,4,5,6,7,8,],
            [0,1,2,3,4,5,6,7,8,],
            [0,1,2,3,4,5,6,7,8,],
            [0,1,2,3,4,5,6,7,8,],
            ]
    act_op = board.from_string(in_put)
    assert len(act_op) == 9
    print(act_op)
    for yy, row in enumerate(act_op):
        for xx, cell in enumerate(row):
            assert len(row) == len(expected_out_put[yy])
            assert cell == expected_out_put[yy][xx]
