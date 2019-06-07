import sympy as sp
import numpy as np



matrizA = np.random.randint(10, size=(10,10))
matrizB = np.random.randint(10, size=(10,10))

#Ejercicio 1
print("Matriz A")
print(matrizA)
print("-----------------------")
print("Matriz B")
print ( matrizB)
#Ejercicio 2
print("Cambio de valores de la diagonal principal de la matriz A")
np.fill_diagonal(matrizA,0)
print(matrizA)
print("-----------------------")
print("Cambio de valores de la diagonal principal de la matriz B")
np.fill_diagonal(matrizB,1)
print(matrizB)
#Ejercicio 3
print("suma entre matriz a y matriz B \n" + str(matrizA+matrizB))
print("------------------------------")
print("Resta entre matriz a y matriz B \n" + str(matrizA-matrizB))
print("------------------------------")
print("Multiplicacion entre matriz a y matriz B \n" + str(matrizA*matrizB))
print("------------------------------")
print("Producto punto  entre matriz A y matriz\n" + str(np.dot(matrizA,matrizB)))
print("------------------------------") 

Mat1 = np.arange(3)
Mat2 = 1 + Mat1
print("Matriz 1 \n" + str(Mat1) + " \nMatriz 2\n " + str(Mat2))
print("producto cruz " + str(np.cross(Mat1,Mat2)))

print("------------------------------") 
print("La matriz transpuesta de A es: \n" + str(matrizA.transpose()))
print("------------------------------") 

print("La matriz transpuesta de B es: \n" + str(matrizB.transpose()))
print("FERR de A")
print(str(sp.Matrix(matrizA).rref()))
print("------------------------------") 
print(str(sp.Matrix(matrizB).rref()))


