import numpy as np
from sympy import *

alpha_list = [-2, -1, 1, 2]
for alpha in alpha_list:
    #H = Matrix([[1, 0, 2*alpha, 0],
    #            [0, -1, 0, 0],
    #            [0, 0, -1, 0],
    #            [0, 2*alpha, 0, 1]
    #            ])
    H = Matrix([
        [1, 1.5, 1.5, 0],
        [0.5, -0.5, 0, 1],
        [0.5, 0, -1, 0.5],
        [0, 1.5, 1.5, 1]
    ])
    P, D = H.diagonalize()

    print(f"Alpha: {alpha}; Diagonal of a matrix : {D}; OG Matrix: {H}")

print("------------------------------")

