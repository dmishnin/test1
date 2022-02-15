import numpy as np
#используется библиотека numpy и присваивается аллиас "np"
#для установки библиотеки "python -n pip install numpy" - для Windows и  "python3 -n pip install numpy" - Linux

a1 = np.random.randint(0, 11, size=(10, 10))
print ('исходная матрица')
for im in range(10):
    print(a1[im])
print('_________')

def decompose_to_LU(a):
    ##Разложить матрицу коэффициентов на матрицы L и U.
    #   Треугольные матрицы L и U будут представлены одной матрицей размера nxn.
    #    :param a: пустая матрица коэффициентов
    #   :return: пустая матрица LU
    
    # создать пустую LU-матрицу
    lu_matrix = np.matrix(np.zeros([a.shape[0], a.shape[1]]))
    n = a.shape[0]
#    print(n)

    for k in range(n):
        # вычисляем все остаточные элементы k-го ряда
        for j in range(k, n):
            lu_matrix[k, j] = a[k, j] - lu_matrix[k, :k] * lu_matrix[:k, j]
        # вычисляем все остаточные элементы k-столбца
        for i in range(k + 1, n):
            lu_matrix[i, k] = (a[i, k] - lu_matrix[i, : k] * lu_matrix[: k, k]) / lu_matrix[k, k]

    return lu_matrix

def get_L(m):
    #Получить треугольную L-матрицу из одной LU-матрицы
    #:param m: numpy LU-матрица
    #:return: пустая треугольная матрица L

    L = m.copy()
    for i in range(L.shape[0]):
            L[i, i] = 1
            L[i, i+1 :] = 0
    return np.matrix(L)


def get_U(m):
    #Получить треугольную U-матрицу из одной LU-матрицы
    #:param m: numpy LU-матрица
    #:return: пустая треугольная матрица U

    U = m.copy()
    for i in range(1, U.shape[0]):
        U[i, :i] = 0
    return U

LU = decompose_to_LU(a1)
L = get_L(LU)
U = get_U(LU)

#LUmulFloat = L * U
#проверка разложения матрицы через перемножение L и U
LUmult = np.rint(L * U)
for im in range(10):
#вывод матрицы после перемножения L * U
    print(LUmult[im])
print("_______")
#Сравнение с исходной матрицей
print (LUmult == a1)