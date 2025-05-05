from math import *

g4 = comb(9, 4) + comb(9, 2) ** 2 + comb(9, 1) * comb(9, 3) + comb(9, 1) ** 2 * comb(9, 2)
g3 = comb(9, 3) + comb(9, 1) * comb(9, 2) + comb(9, 1) ** 3
g2 = comb(9, 2) + comb(9, 1) ** 2
g1 = comb(9, 1)

c4 = g4 + g2 ** 2 + g1 * g3 + g1 ** 2 * g2
c3 = g3 + g1 * g2 + g1 ** 3
c2 = g2 + g1 ** 2
c1 = g1
print(c4, 15 * c4)
print(c3, 15 * c3)
print(c2, 15 * c2)
print(c1, 15 * c1)