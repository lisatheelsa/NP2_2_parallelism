from multiprocessing import Process, Pool
import numpy as np

def element(args):

    index, A, B = args[0], args[1], args[2]
    i, j = index
    res = 0

    N = A.shape[1] or B.shape[0]
    for k in range(N):
        res += A[i, k] * B[k, j]
    return res

def check_matrix(matrix1, matrix2):

    if matrix1.shape[1]==matrix2.shape[0]:
        return True
    else:
        print("Такие матрицы нельзя перемножить!")


def generate_map(mt1, mt2):

    args = []
    for i in range(mt1.shape[0]):
        for j in range(mt2.shape[1]):
            args.append(((i, j), mt1, mt2))

    return args


def write_result_to_file(matrix, filename):

    file = open(filename, 'w')
    for line in matrix:
        for elem in line:
            file.write(f'{elem}\t')
        file.write('\n')
    file.close()


if __name__ == "__main__":
    matrix1 = [[-1, 11, 3, 21],[12, 8, -5, 2]]
    matrix2 = [[-8, 1, 12],[45, 11, 23],[13, -22, 34],[14, 34, -1]]

    p = Pool(matrix1.shape[0] * matrix2.shape[1])

    if check_matrix(matrix1, matrix2):

        args = generate_map(matrix1, matrix2)
        result = np.array(p.map(element, args))
        matrix = result.reshape(matrix1.shape[0], matrix2.shape[1])

        print(matrix)

