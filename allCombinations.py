from itertools import combinations 
import sys

N=8 #Chess table of NxN
for y in combinations([x for x in range(N**2)],N):

