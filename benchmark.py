from sudoku import solve_sudoku
import time
import random
import numpy as np

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

def testClues(n, c):
    times = []
    for i in range(c):
        clues = []
        pos = []
        blank = [-1 for i in range(81)]
        while n > 0:
            i = random.randint(0, 80)
            j = random.randint(1, 9)
            if not (i in pos):
                pos.append(i)
                clues.append(j)
                n -= 1
        if cluesValid(clues, pos):
            for i, j in enumerate(pos):
                blank[j] = clues[i]
            board = [blank[i * 9:(i + 1) * 9] for i in range(9)]
            start = time.time()
            solve_sudoku(board)
            times.append(time.time() - start)
    return times


results = [v for v in [testClues(random.randint(1,4), 100) for i in range(10)]]
print("Average time for 4 clues: ", np.mean(results))
print("Standard deviation for 4 clues: ", np.std(results))
