# Verifies that each n-clue set of lists maps to all permutations
# of 1, 2, 3, and 4 clue lists
import math

testSet = [
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

def enum(val, distinct, dInd, enumerated):
    domain = [i for i in range(1, 10) if not i in val]
    if len(val) == len(distinct) - 1:
        val.append(0)
        for v in domain:
            val[len(distinct) - 1] = v
            digits = [0 for i in range(4)]
            for i0, a in enumerate(dInd):
                for i in a:
                    digits[i] = val[i0]

            num = 0
            for d in digits:
                num = num * 10 + d
            enumerated[num] = True
    else:
        for v in domain:
            enum(val + [v], distinct, dInd, enumerated)

def testEnum(test, enumerated):
    distinct = list(set(test))
    dInd = [0 for i in range(len(test))]
    for i, n in enumerate(test):
        if dInd[n - 1] == 0:
            dInd[n - 1] = []
        dInd[n - 1].append(i)
    dInd = [indices for indices in dInd if indices != 0]
    
    enum([], distinct, dInd, enumerated)

def writeToFile(lst, filename):
    with open(filename, "w") as file:
        for num in lst:
            file.write(f"{num}\n")

def verify(enumerated, enunwriteToFile=True, halt=False, digits=4):
    enumerated_list = list(enumerated.keys())
    enumerated_list.sort()
    if writeToFile:
        writeToFile(enumerated_list, "enumerated.txt")
    
    i = int(1/9 * 10 ** digits)
    while i < 10 ** digits:
        if str(i).find('0') == -1 and not i in enumerated:
            print(f"missing: {i}")
            if halt:
                return False
        i += 1

    return True
    
def verifyMinimum():
    for i in range(len(testSet)):
        copy = testSet.copy()
        copy.pop(i)
        enumerated = {}
        for test in copy:
            testEnum(test, enumerated)

        if verify(enumerated, False, True):
            print('test set can be reduced to ', testSet[i])
            return False

    return True

enumer = {}
for test in testSet:
    testEnum(test, enumer)

verify(enumer, False, False, 4)

enumer = {}
for test in [[1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [1, 2, 3]]:
    testEnum(test, enumer)

verify(enumer, False, False, 3)

# print('verifying minimum...')
# verifyMinimum()