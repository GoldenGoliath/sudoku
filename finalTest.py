import time
from sudoku import solve_sudoku

valid = 0
solvable = 0
total = 0
blank = [-1 for i in range(81)]
def action():
    global total
    total += 1

def cluesValid(clues, pos):
    x = []
    y = []
    for i in range(len(pos)):
        x.append(pos[i] // 9)
        y.append(pos[i] % 9)
    for i in range(len(clues) - 1):
        for j in range(i + 1, len(clues)):
            if clues[i] == clues[j] and (x[i] == x[j] or y[i] == y[j] or ((x[i] // 3) == (x[j] // 3) and (y[i] // 3) == (y[j] // 3))):
                return False
    return True

def testBoard(clues, pos):
    global blank, valid, total, solvable
    total += 1
    if cluesValid(clues, pos):
        valid += 1
        copy = blank.copy()
        for i, p in enumerate(pos):
            copy[p] = clues[i]
        board = [copy[(i * 9):(i + 1) * 9] for i in range(9)]
        if solve_sudoku(board):
            solvable += 1
        else:
            print('UNSOLVABLE!!!!!!')
            print(clues, pos)

    
    return True
    
def r1(clues, func, offset, pos):
    for i in range(offset[0], offset[0] + 9):
        copy = pos.copy() + [i]
        if len(func) > 0:
            func[0](clues, func[1:], offset[1:], copy)
        else:
            testBoard(clues, copy)

def r2(clues, func, offset, pos):
    for i in range(offset[0], offset[0] + 8):
        for j in range(i + 1, offset[0] + 9):
            copy = pos.copy() + [i, j]
            if len(func) > 0:
                func[0](clues, func[1:], offset[1:], copy)
            else:
                testBoard(clues, copy)

def r3(clues, func, offset, pos):
    for i in range(offset[0], offset[0] + 7):
        for j in range(i + 1, offset[0] + 8):
            for k in range(j + 1, offset[0] + 9):
                copy = pos.copy() + [i, j, k]
                if len(func) > 0:
                    func[0](clues, func[1:], offset[1:], copy)
                else:
                    testBoard(clues, copy)

def r4(clues, func, offset, pos):
    for i in range(offset[0], offset[0] + 6):
        for j in range(i + 1, offset[0] + 7):
            for k in range(j + 1, offset[0] + 8):
                for l in range(k + 1, offset[0] + 9):
                    copy = pos.copy() + [i, j, k, l]
                    if cluesValid(clues, copy):
                        testBoard(clues, copy)

def g1(clues, func, offset, pos):
    r1(clues, func, offset, pos)

def g2(clues, func, offset, pos):
    r2(clues, func, offset, pos)
    r1(clues, [r1] + func, [9] + offset, pos)

def g3(clues, func, offset, pos):
    r3(clues, func, offset, pos)
    r1(clues, [r2] + func, [9] + offset, pos)
    r1(clues, [r1, r1] + func, [9, 18] + offset, pos)

def g4(clues, func, offset, pos):
    r4(clues, func, offset, pos)
    r1(clues, [r3] + func, [9] + offset, pos)
    r2(clues, [r2] + func, [9] + offset, pos)
    r1(clues, [r1, r2] + func, [9, 18] + offset, pos)

def testClue(clue):
    if len(clue) == 1:
        g1(clue, [], [0], [])
    elif len(clue) == 2:
        g2(clue, [], [0], [])
        g1(clue, [g1], [0, 27], [])
    elif len(clue) == 3:
        g3(clue, [], [0], [])
        g1(clue, [g2], [0, 27], [])
        g1(clue, [g1, g1], [0, 27, 54], [])
    elif len(clue) == 4:
        g4(clue, [], [0], [])
        g1(clue, [g3], [0, 27], [])
        g2(clue, [g2], [0, 27], [])
        g1(clue, [g1, g2], [0, 27, 54], [])

oneClue = [[1]]
twoClue = [
    [1, 1],
    [1, 2]
]
threeClue = [
    [1, 1, 1],
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1],
    [1, 2, 3]
]
fourClue = [
    [1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 1, 2, 1],
    [1, 2, 1, 1],
    [2, 1, 1, 1],
    [1, 2, 2, 1],
    [2, 2, 1, 1],
    [1, 2, 1, 2],
    [1, 2, 3, 3],
    [1, 3, 3, 2],
    [3, 3, 1, 2],
    [3, 1, 2, 3],
    [3, 1, 3, 2],
    [1, 3, 2, 3],
    [1, 2, 3, 4],
]

def testClues(clueSet):
    start = time.time()
    global valid, solvable, total
    valid = 0
    solvable = 0
    total = 0
    for clue in clueSet:
        testClue(clue)
    end = time.time()
    print(f'Test results for {len(clueSet[0])} clue sudoku boards')
    print('Valid:', valid)
    print('Solvable:', solvable)
    print('Total:', total)
    print('Total time elapsed:', end-start)

testClues(oneClue)
testClues(twoClue)
testClues(threeClue)
testClues(fourClue)