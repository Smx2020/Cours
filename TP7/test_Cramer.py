from Cramer import *
import numpy as np

Ab = [[2,2,-3],[-2,-1,-3],[6,4,4]]
Ac = [2,-5,16]

print(Resolution(Ab,Ac))
print(np.linalg.solve(Ab,Ac))
