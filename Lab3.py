import numpy as np
import sympy as sp
import matplotlib
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt

def Aumentar(a):
    Valor='h'+str(sp.Matrix(a).shape)
    Identidad=sp.eye(int(Valor[2]))
    for x in range(0, int(Valor[2])):
        Identidad=Identidad.col_insert(x, sp.Matrix(a).col(x))
    return Identidad


A = np.array([[1,1,0],
             [1,0,1],
             [0,1,0]])

B = np.array([[2,0,1],
             [1,1,-4],
             [3,7,-3]])

C = np.array([[1,1,0],
             [1,0,1],
             [0,1,0],
             [0,1,0]])


print("Inversa de matriz A usando tres métodos \n")
InvA = np.linalg.inv(A)
print("_________________________________________________\n")
print("Inversa utilizando numpy:\n" + str(InvA))
InvA2 = sp.Matrix(A).inv()
print("_________________________________________________\n")
print("Inversa utilizando sympy:\n" + str(InvA2))
Inva3 = Aumentar(A).rref()
print("_________________________________________________\n")

print("Inversa con FERR:\n" + str(Inva3))
print("_________________________________________________\n")

print("Inversa de matriz B usando tres métodos \n")
InvB = np.linalg.inv(B)
print("_________________________________________________\n")
print("Inversa utilizando numpy:\n" + str(InvB))
InvB2 = sp.Matrix(B).inv()
print("_________________________________________________\n")
print("Inversa utilizando sympy:\n" + str(InvA2))
InvB3 = Aumentar(B).rref()
print("_________________________________________________\n")

print("Inversa con FERR:\n" + str(InvB3))
print("_________________________________________________\n")
print("La diferencia entre las tres librerías es que la librería numpy lo imprime con decimales, sympy con numeros enteros y FERR lo imprime con fracciones.")

print("No se puede hacer la inversa de la matriz C porque no es cuadrada \n")


print("EJERCICIO 2 y 3")
Rango = np.linalg.matrix_rank(A)
Numcols = A.shape[1]

Nulidad = Rango - Numcols

print(" Rango y Nulidad de la Matriz A \n")
print("# Columnas:  " +str(Numcols) )
print("Rango:       " +str(Rango))            
print("Nulidad:     " +str(Nulidad))

RangoB = np.linalg.matrix_rank(B)
NumcolsB = B.shape[1]
NulidadB = RangoB - NumcolsB
print(" Rango y Nulidad de la Matriz B \n")
print("# Columnas:  " +str(NumcolsB) )
print("Rango:       " +str(RangoB))            
print("Nulidad:     " +str(NulidadB))

RangoC = np.linalg.matrix_rank(C)
NumcolsC = C.shape[1]
NulidadC = RangoC - NumcolsC
print(" Rango y Nulidad de la Matriz C \n")
print("# Columnas:  " +str(NumcolsC) )
print("Rango:       " +str(RangoC))            
print("Nulidad:     " +str(NulidadC))
print("\n")

print("En los tres casos me queda que el rango es de 3 porque es el número máximo de columnas que son linealmente independientes\n")
print("Ejercicio 4")

def f(x):
    return 1-x
def g(x):
    return x-4
def h(x):
    return x+4
def k(x):
    return 6-x

x = range(-10,10)
plt.plot(x,[f(i) for i in x])
plt.plot(x,[g(i) for i in x])
plt.plot(x,[h(i) for i in x])
plt.plot(x,[k(i) for i in x])


plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(-11, 11)
plt.ylim(-11, 11)

plt.title("Graficas ")
plt.xlabel("Eje x")
plt.ylabel("Eje Y")
plt.grid()
plt.legend(('F(x): 1 -x ','G(x): x-4 ','H(x): x+4 ','K(x): 6-x '),prop = {'size':10}, loc ='upper right')
plt.figure(figsize=(12,5))


plt.show()
plt.savefig("Graficas.png")

#No se porqué se guarda un archivo con el nombre "Graficas" que está vacío como figure 2.