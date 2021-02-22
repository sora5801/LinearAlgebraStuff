from sympy import *
import random
from matplotlib import pyplot as plt
import numpy as np
from numpy import linalg as LA

m = 0
i = int(input("Input 1 to input a matrix. Input 2 to randomly generate a matrix."))
if (i == 1):
    r = int(input("How many rows will there be? "))
    c = int(input("How many columns will there be? "))
    j = 0  # amount of elements in matrix counter
    k = 0  # columns counter
    g = 0  # row counters
    list = []
    while j < r * c:
        # counts starts at 0
        l = input("What will ({},{}) be? Press d to delete previous.".format(g, k))
        if l == 'd':
            list.pop()
            j -= 1
            if g > 0 and k == 0:
                g -= 1
                k = c - 1
                continue
            k -= 1
            continue
        k += 1
        if k == c:
            k = 0
            g += 1
        list.append(float(l))
        j += 1
    print(list)
    m = Matrix(r, c, list)
if (i == 2):
    r = int(input("How many rows will there be? "))
    c = int(input("How many columns will there be? "))
    randomlist = []
    for i in range(0, r * c):
        n = random.randint(1, 10)
        randomlist.append(n)
    m = Matrix(r, c, randomlist)
'''
r = int(input("How many rows will there be? "))
c = int(input("How many columns will there be? "))
randomlist = []
for i in range(0, r * c):
    n = random.randint(1, 8)
    randomlist.append(n)
m = Matrix(r, c, randomlist)
'''
L, U, _ = m.LUdecomposition()
print(list(m.row(0)))
print("The matrix is {}".format(m))
print("The lower triangular matrix m is {}".format(L))
print("The upper triangular matrix m is {}".format(U))
print("The echelon form of matrix m is {}.".format(m.echelon_form()))
print("The Row reduced echelon form of matrix M and the pivot columns : {}".format(m.rref()))
print("The Rank of matrix m is {}".format(m.rank()))
print("The column space of matrix m is {}".format(m.columnspace()))
print("The row space of matrix m is {}".format(m.rowspace()))
print("The null space of matrix m is {}.".format(m.nullspace()))
print("The null space of the transpose of matrix m is {}".format(m.T.nullspace()))
'''
if r == 2:  # The number of rows represent the "features" such as height and weight. Currently setting that to two
    A = m * ones(m.shape[1], 1)  # The columns are the number of measurements
    v = []
    for i in range(0, c):
        v.append(A[0])
    for i in range(0, c):
        v.append(A[1])
    L = Matrix(r, c, v) / c
    Cov = ((m - L) * (m - L).T) / (c - 1)  # The covariance matrix
    print("The sample covariance matrix is {}".format(Cov))
    print("The eigenvalues of the covariance matrix are {}".format(Cov.eigenvals()))
    print("The eigenvectors of the covariance matrix are {}".format(Cov.eigenvects()))
    print(np.array(Cov.eigenvects()[0][2][0]))
    print(np.array(Cov.eigenvects()[1][2][0]))
    print(np.array(Cov.eigenvects()[1][2][0].row(0))[0][0])
    print(np.array(Cov.eigenvects()[1][2][0].row(1))[0][0])
    # The eigenvectors of the covariance matrix are it's "principal components"
    # eigen_values, eigen_vectors = LA.eig(np.array(Cov))
    # eig_vec1 = eigen_vectors[:, 0]
    # eig_vec2 = eigen_vectors[:, 1]
    origin = [0, 0]
    a = np.array(Cov.eigenvects()[1][2][0].row(0))[0][0]
    b = np.array(Cov.eigenvects()[1][2][0].row(1))[0][0]
    c = np.array(Cov.eigenvects()[0][2][0].row(0))[0][0]
    d = np.array(Cov.eigenvects()[0][2][0].row(1))[0][0]
    C = float(a)
    D = float(b)
    E = float(c)
    F = float(d)
    vector1 = [C, E]
    vector2 = [D, F]
    plt.scatter(np.array(m.row(0)), np.array(m.row(1)))
    plt.quiver(*origin, np.array(vector1), np.array(vector2), color=['r', 'b'], scale = 0.5)
    plt.xlim(-4, 14)
    plt.ylim(-4, 14)
    plt.show()
'''
if r == c:
    print("The determinant of matrix m is {}".format(m.det()))
    Q, R = m.QRdecomposition()
    print("The Q matrix of m is {}".format(Q))  # Q is an orthogonal matrix
    print("The R matrix of m is {}".format(R))  # R is an upper triangular matrix
    # print("The eigenvalues and eigenvectors of m is {}".format(m.eigenvects())) #This has issues starting from 3x3 matr

if m.rank() == c:
    print("The matrix m has full column rank and therefore has no free variables and therefore has independent "
          "columns (rank is equal to column amount)")
if m.rank() == r:
    print("The matrix m has full row rank, there are 2 special solutions(r-rank)  (rank is equal to row amount)")
if r == c and m.det() != 0:
    print("The inverse of matrix m is {}".format(m.inv()))
if (m.T * m).det() != 0:
    p = m * (m.T * m).inv() * m.T
    print("The projection matrix of m is {}".format(p))

print("The dimension of the row space and column space of matrix m is {}".format(m.rank()))
print("The dimension of the nullspace is {}".format(c - m.rank()))
print("The dimension of the nullspace of the transpose(left-nullspace) is {}".format(r - m.rank()))

'''
By the fundamental theorem of linear algebra part 1
The column space and row space both have dimension rank(m)
The nullspace has dimensions c - rank(m) and the nullspace of the transpose(left-nullspace) has r - rank(m)

By the fundamental theorem of linear algebra part 2
The row space is perpendicular to the nullspace
The column space is perpendicular to the nullspace of the transpose

The projection p of a vector b onto the line through a is the closest point p = a(a.T * b/a.T* a)
'''
