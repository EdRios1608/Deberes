#!/usr/bin/env python
# coding: utf-8

# In[4]:


from typing import List

class Ejercicio1:
    def crearIslas(self, r, c, isla, posF, posC):

        for arreglo in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            fila = r+arreglo[0]
            col = c+arreglo[1]

            if ((0 <= fila< posF) and (0 <= col < posC) and (isla[fila][col] == '1')): #ver si son adiacentes
                isla[fila][col] = '0'
                self.crearIslas(fila, col, isla, posF, posC)

    def conteoNum(self, isla: List[List[str]]):
        posF = len(isla)
        posC = len(isla[0])
        conteoIslas = 0

        for i in range(posF):
            for j in range(posC):
                if isla[i][j]=='1':
                    conteoIslas += 1
                    self.crearIslas(i, j, isla, posF, posC)
        return conteoIslas

obj = Ejercicio1()
print(obj.conteoNum([["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]]))


# In[3]:


def Ejercicio2(numero):
    arregloNumeros = []
    conteoCuadradosPerfectos = 1

    while (conteoCuadradosPerfectos * conteoCuadradosPerfectos <= numero):
        multiplicacion = conteoCuadradosPerfectos*conteoCuadradosPerfectos
        arregloNumeros.append(multiplicacion) #Ponemos los numeros en el arreglo
        conteoCuadradosPerfectos += 1

    numMinimoMult = [float("inf") for _ in range(numero + 1)] 
    numMinimoMult[0] = 0

    for i in range(numero + 1):
        for j in arregloNumeros:
            if(i - j >= 0): # Vemos si es cuadrado perfecto 
                numMinimoMult[i] = min(numMinimoMult[i], numMinimoMult[i - j] + 1)

    return numMinimoMult[numero]

print(Ejercicio2(20)) 

