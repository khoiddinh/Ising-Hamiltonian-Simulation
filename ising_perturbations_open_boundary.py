import numpy as np

Z = np.array([[1, 0], [0, -1]])
X = np.array([[0, 1], [1, 0]])
I = np.array([[1, 0], [0, 1]])
alpha = 1

for n in range(2, 12):
    N = n
    total_matrix_sum = np.zeros((2**N, 2**N))
    for idx in range(N-1):
        m_list = [I for _ in range(N)]
        m_list[idx] = Z
        m_list[idx+1] = Z
        curr_matrix = m_list[0]
        for i in range(1, N):
            curr_matrix = np.kron(curr_matrix, m_list[i])
        total_matrix_sum += curr_matrix

    #print(total_matrix_sum)
    l = []
    for row in total_matrix_sum:
        for elem in row:
            if elem != 0:
                l.append(int(elem))
                break
        else:
            l.append(0)
    assert len(l) == 2**n
    ev = np.linalg.eig(total_matrix_sum)
    vals = ev[0]
    vectors = ev[1]
    print(f"N = {n}; Diagonal: {l}")
    print(f"{np.unique(vals)}")
    print(f"Number of eigen values {np.unique(vals).shape[0]}")
    eigen_vectors = []
    for i, e_val in enumerate(vals):
        ev = np.argmax(vectors[:, i]) + 1
        if ev not in eigen_vectors:
            eigen_vectors.append(ev)
    print(f"Number of eigen vectors: {len(eigen_vectors)}")
    print("_______________________")

