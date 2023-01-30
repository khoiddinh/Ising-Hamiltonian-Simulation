import numpy as np

Z = np.array([[1, 0], [0, -1]])
I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])

def tensor(op):
    curr = op[0]
    for i, pauli in enumerate(op):
        if i==0: continue
        curr = np.kron(curr, pauli)
    return np.abs(curr)

_op1 = [X, I, I, X]
_op2 = [I, Z, Z]

e = tensor(_op1)
f = tensor(_op2)
g = tensor([e, f])
h = tensor([f, e])
output = (g==h)
print(np.all(output))

f = tensor([X, X])
g = tensor([X, I]) + tensor([I, X])
print(f)
print(g)
