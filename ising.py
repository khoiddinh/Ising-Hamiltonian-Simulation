import numpy as np

Z = np.array([[1, 0], [0, -1]]) 
I = np.array([[1, 0], [0, 1]])

for n in range(2, 12):  # loop over from N=2 to N=11 case
    N = n
    total_matrix_sum = np.zeros((2**N, 2**N))
    for idx in range(N-1):  # loop over summation
        m_list = [I for _ in range(N)]
        m_list[idx] = Z
        m_list[idx+1] = Z
        curr_matrix = m_list[0]
        for i in range(1, N):  # tensor each element in summation
            curr_matrix = np.kron(curr_matrix, m_list[i])
        total_matrix_sum += curr_matrix

    diagonal = []
    for row in total_matrix_sum:  # quick way of flattening array to diagonal 1d array
        for elem in row:
            if elem != 0:
                diagonal.append(int(elem))
                break
        else:
            diagonal.append(0)
    assert len(diagonal) == 2**n  # check matrix size
    ev = np.linalg.eig(total_matrix_sum)
    vals = ev[0]
    vectors = ev[1]
    print(f"N = {n}; Diagonal: {diagonal}")
    print(f"{np.unique(vals)}")
    print(f"Number of eigen values {np.unique(vals).shape[0]}")
    eigen_vectors = []
    for i, e_val in enumerate(vals):
        ev = np.argmax(vectors[:, i]) + 1  # math index (1 based) for eigen vector: [0, 1, 0] -> 2
        if ev not in eigen_vectors:
            eigen_vectors.append(ev)
    print(f"Number of eigen vectors: {len(eigen_vectors)}")
    print("_______________________")

