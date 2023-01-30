import numpy as np
import scipy as sp
from qiskit import Aer
from qiskit.opflow import PauliTrotterEvolution, StateFn, PauliExpectation
from qiskit.opflow import CircuitSampler, PauliOp
from qiskit.opflow import I, X, Y, Z, Zero, One, Plus, Minus
from qiskit.circuit import Parameter

hamiltonian = (Z^Z)
evo_time = Parameter('t')
evolution_op = (evo_time*hamiltonian).exp_i()
num_time_slices = 1
trotterized_op = PauliTrotterEvolution(
                    trotter_mode='trotter',
                    reps=num_time_slices).convert(evolution_op)
trotterized_op.to_circuit().draw(output='mpl')