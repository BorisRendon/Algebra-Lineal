import numpy as np
import sympy as sp

A = np.array([[1,1,0],
             [1,0,1],
             [0,1,0]])

B = np.array([[2,0,1,1],
             [1,1,2,0],
             [3,7,-3,1]])

C = np.array([[1,1,0,1],
             [1,0,1,0],
             [0,1,0,0],
             [0,1,0,0]])


print("Determinantes usando NUMPY")
DETA = np.linalg.det(A)
print("Determinante matriz A: \n" + str(DETA))
print("\n")
DETB = np.linalg.det(B)
print("Determinante matriz B: \n" + str(DETB))
print("\n")
DETC = np.linalg.det(C)
print("Determinante matriz C: \n" + str(DETC))
print("\n")
print("---------------------------------------------------------")
Deta2 = sp.Matrix(A).det()
Detb2 = sp.Matrix(B).det()
DetC2 = sp.Matrix(C).det()
print("DETERMINANTES USANDO SYMPY")
print("Determinante matriz A: \n" + str(Deta2))
print("\n")

print("Determinante matriz B: \n" + str(Detb2))
print("\n")

print("Determinante matriz C: \n" + str(DetC2))
print("\n")
print("---------------------------------------------------------")
print("La diferencia entre usar numpy y sympy es: ")

print("Ejercicio 3 , eigenvectores y eigenvalores")
print("NUMPY")
EIG = np.linalg.eigvals(A)
print("\n Eigenvalores con numpy: \n " + str(EIG))
EIGC = np.linalg.eigvals(C)
print("\n Eigenvalores con numpy: \n " + str(EIGC))

EIGVAL, EIGVEC = np.linalg.eig(A)
print("\n Eigenvectores con numpy: \n " + str(EIGVEC))
print("---------------------------------------------------------")
print("SYMPY")
eig2 = sp.Matrix(A).eigenvals()
print("Eigenvalores : \n" + str(eig2))
eig3 = sp.Matrix(C).eigenvals()
print("---------------------------------------------------------")

DIAG = sp.Matrix(A).diagonalize()
print("Diagonalización sympy de matriz A: \n" + str(DIAG))
DIAGC = sp.Matrix(C).diagonalize()
print("Diagonalización sympy de matriz C: \n" + str(DIAGC))
print("---------------------------------------------------------")
POLA = sp.Matrix(A).charpoly()
print("\n Polinomio caracteristico: \n " + str(POLA))
POLC = sp.Matrix(C).charpoly()
print("\n Polinomio caracteristico: \n " + str(POLC))








