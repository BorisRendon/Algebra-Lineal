
#Ejercicio1
num1 =4
num2 =2
resultado= num1 + num2
print(num1,num2,resultado)
print("")
#Ejercicio2 y Ejercicio3
Resultado=[num1+num2,num1-num2,num1*num2,num1/num2, num1^2]
print(Resultado)
print("El resultado de la suma es: ")
print(Resultado[0])
print("")

print("El resultado de la resta es: ")
print(Resultado[1])
print("")

print("El resultado de la multiplicación es: ")
print(Resultado[2])
print("")

print("El resultado de la división es: ")
print(Resultado[3])
print("")

print("El resultado de la potencia del primer numero es: ")
print(Resultado[4])
print("")

#Ejercicio4
print("El resultado de la matriz 5x5 es el siguiente: ")
Mat5= [[1,2,3,4,5],
       [5,4,3,2,1],
       [9,8,7,6,5],
       [2,3,1,5,1],
       [9,9,9,5,6]]
#Ejercicio5
for i in Mat5:
    print(i)
print("")

#Ejercicio6

MatNueva = Mat5
MatNueva[0][0] = 0
MatNueva[1][1] = 0
MatNueva[2][2] = 0
MatNueva[3][3] = 0
MatNueva[4][4] = 0

#Ejercicio7
print("El resultado de la matriz nueva cambiando la diagonal principal es: ")
for k in MatNueva:
       print(k)