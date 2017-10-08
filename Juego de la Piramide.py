# -*- coding: utf-8 -*-
import math
import os
class Ficha:
    def __init__(self, valor=0, x1=None, y1=None, x2=None, y2=None):
        self.valor = valor
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Tabla:
    def __init__(self, tabla, padre=None):
        self.tabla = tabla
        self.padre = padre
        self.hijos = None
        self.h = None
        self.g = None
        
    def __str__(self):
        t = ""
        for columna in self.tabla:
            for ficha in columna:
                t += str(ficha.valor)
                t += '\n'
        return t
        
    def generaHijos_J1(self):
        self.hijos = []
        copy = copia(self.tabla)
         
        for i in range(0, 8):
            for j in range(0, 8):
                if copy[i][j].valor == 1:

                    if i < 8-1 and j >= 1: 
                        if copy[i+1][j-1].valor == 0:
                            temp = copia(copy)
                            t = temp[i][j]
                            #temp[i][j] = 0
                            temp[i][j] = temp[i+1][j-1]
                            #temp[i+1][j-1] = 1
                            t.y1 = i+1
                            t.x1 = j-1
                            temp[i+1][j-1] = t
                            self.hijos.append(Tabla(temp, self))
                        else:
                            if i < 8-2 and j >= 2:
                                if copy[i+2][j-2].valor == 0:
                                    temp = copia(copy)
                                    t = temp[i][j]
                                    #temp[i][j] = 0
                                    temp[i][j] = temp[i+2][j-2]
                                    #temp[i+2][j-2] = 1
                                    t.y1 = i+2
                                    t.x1 = j-2
                                    temp[i+2][j-2] = t
                                    self.hijos.append(Tabla(temp, self))
                                    
                    if i < 8-1 and j < 8-1:
                        if copy[i+1][j+1].valor == 0:
                            temp = copia(copy)
                            t = temp[i][j]
                            #temp[i][j] = 0
                            temp[i][j] = temp[i+1][j+1]
                            #temp[i+1][j+1] = 1
                            t.y1 = i+1
                            t.x1 = j+1
                            temp[i+1][j+1] = t
                            self.hijos.append(Tabla(temp, self))
                        else:
                            if i < 8-2 and j < 8-2:
                                if copy[i+2][j+2].valor == 0:
                                    temp = copia(copy)
                                    t = temp[i][j]
                                    #temp[i][j] = 0
                                    temp[i][j] = temp[i+2][j+2]
                                    #temp[i+2][j+2] = 1
                                    t.y1 = i+2
                                    t.x1 = j+2
                                    temp[i+2][j+2] = t
                                    self.hijos.append(Tabla(temp, self))
                                    
    def generaHijos_J2(self):
        self.hijos = []
        copy = copia(self.tabla)
         
        for i in range(0, 8):
            for j in range(0, 8):
                if copy[i][j].valor == 2:

                    if i >= 1 and j >= 1: 
                        if copy[i-1][j-1].valor == 0:
                            temp = copia(copy)
                            t = temp[i][j]
                            #temp[i][j] = 0
                            temp[i][j] = temp[i-1][j-1]
                            #temp[i-1][j-1] = 1
                            t.y1 = i-1
                            t.x1 = j-1
                            temp[i-1][j-1] = t
                            self.hijos.append(Tabla(temp, self))
                        else:
                            if i >= 2 and j >= 2:
                                if copy[i-2][j-2].valor == 0:
                                    temp = copia(copy)
                                    t = temp[i][j]
                                    #temp[i][j] = 0
                                    temp[i][j] = temp[i-2][j-2]
                                    #temp[i-2][j-2] = 1
                                    t.y1 = i-2
                                    t.x1 = j-2
                                    temp[i-2][j-2] = t
                                    self.hijos.append(Tabla(temp, self))
                                    
                    if i >= 1 and j < 8-1:
                        if copy[i-1][j+1].valor == 0:
                            temp = copia(copy)
                            t = temp[i][j]
                            #temp[i][j] = 0
                            temp[i][j] = temp[i-1][j+1]
                            #temp[i-1][j+1] = 1
                            t.y1 = i-1
                            t.x1 = j+1
                            temp[i-1][j+1] = t
                            self.hijos.append(Tabla(temp, self))
                        else:
                            if i >= 2 and j < 8-2:
                                if copy[i-2][j+2].valor == 0:
                                    temp = copia(copy)
                                    t = temp[i][j]
                                    #temp[i][j] = 0
                                    temp[i][j] = temp[i-2][j+2]
                                    #temp[i-2][j+2] = 1
                                    t.y1 = i-2
                                    t.x1 = j+2
                                    temp[i-2][j+2] = t
                                    self.hijos.append(Tabla(temp, self))
                            
                                    
    def getHijos(self):
        return self.hijos
                                    
    def imprimirHijos(self):
        for hijo in self.hijos:            
            print ('\nh(n) = ' + str(hijo.h))
            print ('g(n) = ' + str(hijo.g))
            imprimir(hijo.tabla)

    def calcularHijos_H(self):
        for hijo in self.hijos:
            h = 0
            tabla = hijo.tabla
            for columna in tabla:
                for ficha in columna:
                    if ficha.valor == 1:
                        #h += ficha.x2 - ficha.x1 + ficha.y2 - ficha.y1
                        h += math.sqrt((ficha.x2 - ficha.x1)**2 + (ficha.y2 - ficha.y1)**2)
            hijo.h = h
            
    def calcularHijos_G(self):
        for hijo in self.hijos:
            hijo.g = conseguirG(hijo)
        
def conseguirG(tabla):
    g = 0
    while tabla.padre != None:
        g += 1
        tabla = tabla.padre
    return g
        
            
def copia(tabla):
    t = []
    for columna in tabla:
        temp = []
        for ficha in columna:
            temp.append(Ficha(ficha.valor, ficha.x1, ficha.y1, ficha.x2, ficha.y2))
        t.append(temp)
    return t
                            

def imprimir(tabla):
    t = "   1 2 3 4 5 6 7 8\n\n"
    i = 1
    j = 1
    for columna in tabla:
        t += str(i) + '  ' 
        for ficha in columna:
            if ficha.valor == 0:
                if i % 2 != 0:
                    if j % 2 == 0:
                        c = u"\u2593"
                        #c= c.decode('utf-8')
                        t += c + ' '
                    elif ficha.valor == 0:
                        c = u"\u2591"
                        #c= c.decode('utf-8')
                        t += c + ' '
                elif i % 2 == 0:
                    if j % 2 != 0:
                        c = u"\u2593"
                        #c= c.decode('utf-8')
                        t += c + ' '
                    elif ficha.valor == 0:
                        c = u"\u2591"
                        #c= c.decode('utf-8')
                        t += c + ' '
            else:
                t += str(ficha.valor) + ' '
            j += 1
        t += '\n'
        i += 1
    print (t)    
              
def ganoJ1(tabla):
    '''
    Verifica si Ganó el Jugador 1 (PC)
    '''
    i=0
    j=0
    for columna in tabla.tabla:
        j = 0
        for hijo in columna:
            if i == 7:
                if j == 1 or j == 3 or j == 5 or j == 7:
                    if hijo.valor != 1:
                        return False
            elif i == 6:
                if j == 2 or j == 4 or j == 6:
                    if hijo.valor != 1:
                        return False
                            
            elif i == 5:
                if j == 3 or j == 5:
                    if hijo.valor != 1:
                        return False
                            
            elif i == 4:
                if j == 4:
                    if hijo.valor != 1:
                        return False
            j += 1
        i += 1
    return True
    
def ganoJ2(tabla):
    '''
    Verifica si Ganó el Jugador 2 (Humano)
    '''
    i=0
    j=0
    for columna in tabla.tabla:
        j = 0
        for hijo in columna:
            if i == 0:
                if j == 0 or j == 2 or j == 4 or j == 6:
                    if hijo.valor != 2:
                        return False
            elif i == 1:
                if j == 1 or j == 3 or j == 5:
                    if hijo.valor != 2:
                        return False
                            
            elif i == 2:
                if j == 2 or j == 4:
                    if hijo.valor != 2:
                        return False
                            
            elif i == 3:
                if j == 3:
                    if hijo.valor != 2:
                        return False
            j += 1
        i += 1
    return True
    
def calcularF(tabla):
    '''
    Dada la tabla, retorna f(n)
    Donde f(n) = g(n) + h(n)
    '''
    return tabla.g + tabla.h
    
def ordenarLista(lista):
    '''
    Ordena la lista por el valor de f(n)
    Usa Algoritmo Insertion Sort
    '''
    for i in range(1, len(lista)):
        j = i
        while j > 0 and calcularF(lista[j-1]) > calcularF(lista[j]):
            temp = lista[j]
            lista[j] = lista[j-1]
            lista[j-1] = temp
            j = j - 1

def tieneHijosJ2(tabla):
    ''' 
    Verifica si el jugador 2 tiene hijos
    '''
    tabla.generaHijos_J2()
    hijos = tabla.getHijos()
    t = tabla.tabla

    # verificar si J2 tiene hijos
    if len(hijos) > 0:
        return True
    return False
            
def actualizar(tabla, x1, y1, x2, y2):
    ''' 
    Actualiza el tablero con las jugadas del jugador 2
    '''
    tabla.generaHijos_J2()
    hijos = tabla.getHijos()
    t = tabla.tabla

    for hijo in hijos:
        # verificar si la movida escogida por el usuario es uno de los movimientos
        # válidos de la jugada, es decir verificar si la jugada escogida es un hijo
        # de la tabla actual.
        if hijo.tabla[y1][x1].valor == 0 and hijo.tabla[y2][x2].valor == 2:
            if t[y2][x2].valor == 0 and t[y1][x1].valor == 2:
                temp = t[y2][x2]
                t[y2][x2] = t[y1][x1]
                t[y1][x1] = temp
                return True
    return False
    
    
#tabla1 = [[1, 0, 1, 0, 1, 0, 1, 0], 
#         [0, 1, 0, 1, 0, 1, 0, 0], 
#         [0, 0, 1, 0, 1, 0, 0, 0], 
#         [0, 0, 0, 1, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 2, 0, 0, 0], 
#         [0, 0, 0, 2, 0, 2, 0, 0], 
#         [0, 0, 2, 0, 2, 0, 2, 0], 
#         [0, 2, 0, 2, 0, 2, 0, 2]]

# Tabla inicial del juego        
tabla1 = [[Ficha(1, 0, 0, 4, 4), Ficha(), Ficha(1, 2, 0, 5, 5), Ficha(), Ficha(1, 4, 0, 6, 6), Ficha(), Ficha(1, 6, 0, 7, 7), Ficha()], 
         [Ficha(), Ficha(1, 1, 1, 3, 5), Ficha(), Ficha(1, 3, 1, 4, 6), Ficha(), Ficha(1, 5, 1, 5, 7), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(1, 2, 2, 2, 6), Ficha(), Ficha(1, 4, 2, 3, 7), Ficha(), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(), Ficha(1, 3, 3, 1, 7), Ficha(), Ficha(), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(), Ficha(), Ficha(2), Ficha(), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(), Ficha(2), Ficha(), Ficha(2), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(2), Ficha(), Ficha(2), Ficha(), Ficha(2), Ficha()], 
         [Ficha(), Ficha(2), Ficha(), Ficha(2), Ficha(), Ficha(2), Ficha(), Ficha(2)]]

# Tabla sin fichas contrincantes para probar el algoritmo
tabla2 = [[Ficha(1, 0, 0, 4, 4), Ficha(), Ficha(1, 2, 0, 5, 5), Ficha(), Ficha(1, 4, 0, 6, 6), Ficha(), Ficha(1, 6, 0, 7, 7), Ficha()], 
         [Ficha(), Ficha(1, 1, 1, 3, 5), Ficha(), Ficha(1, 3, 1, 4, 6), Ficha(), Ficha(1, 5, 1, 5, 7), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(1, 2, 2, 2, 6), Ficha(), Ficha(1, 4, 2, 3, 7), Ficha(), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(), Ficha(1, 3, 3, 1, 7), Ficha(), Ficha(), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha()], 
         [Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha(), Ficha()]]
         
os.system("cls")

print ('         Universidad Tecnológica de Panamá')
print ('Facultad de Ingeniería en Sistemas Computacionales')
print ('             Inteligencia Artificial')
print ('                  Proyecto No. 3\n')
print ('       Facilitador: Dr. Euclides Samaniego G.\n')
print ('                   Integrantes:')
print ('                 - Castillo, Kevin')
print ('                 - Herrera, Joel')
print ('                 - Kishinani, Karan')
print ('                 - Visuete, Miguel')

input()
os.system("cls")

a = Tabla(tabla1)

print ('Juego de la Pirámide')
print ('PC (1) vs TU (2)')
print ('El objetivo del juego es ser el primero en reconstruir')
print ('su pirámide en el lado opuesto del tablero.')
print ('Tus Fichas son número 2.\n')
print ('Tablero Inicial:')
imprimir(a.tabla)
input()

#Algoritmo A*
lista = []
lista.append(a)
while len(lista) > 0:
    if not ganoJ1(lista[0]) and not ganoJ2(lista[0]):
        os.system("cls")
        tabla = lista.pop(0)
        tabla.generaHijos_J1()
        tabla.calcularHijos_H()
        tabla.calcularHijos_G()
        hijos = tabla.getHijos()
        for hijo in hijos:
            lista.append(hijo)
        ordenarLista(lista)
        
        #print(calcularF(lista[0]))
        #imprimir(lista[0].tabla)
        
        #for tabla in lista:
        #    print(calcularF(tabla))
        #    imprimir(tabla.tabla)
        
        #Se muestra en pantalla la tabla con la menor f(n)
        #este es el primer elemento de la lista
        tabla = lista[0]
        
        print ('Jugador 1:')
        imprimir(tabla.tabla)
        input()

        
        
        #Jugador 2
        if tieneHijosJ2(tabla):
            while True:
                os.system("cls")
                print ('Jugador 2:')
                imprimir(tabla.tabla)
                try:
                    print ('Ingrese las coordenadas origen y meta de la ficha que desea mover:')
                    print ('\n Origen:')
                    x1 = int(input(' x1 = ')) -1
                    y1 = int(input(' y1 = ')) -1
                    print ('\n Destino:')
                    x2 = int(input(' x2 = ')) -1 
                    y2 = int(input(' y2 = ')) -1
                except ValueError:
                    print ('Ingrese un número válido')
                    input()
                    continue
                
                #Validar numero de ficha
                if not (x1 >= 1 and x1 <= 8) and not (y1 >= 1 and y1 <= 8)\
                    and not (x2 >= 1 and x2 <= 8) and not (y2 >= 1 and y2 <= 8):
                        print ('Ingrese coordenadas válidas')
                        input()
                        continue
                
                #Actualizar fichas del jugador2 en la tabla
                if actualizar(tabla, x1, y1, x2, y2):
                        break
                else:
                    print ('Movimiento no válido')
                    input()
            
            os.system("cls")
            print ('Jugador 2:')       
            imprimir(tabla.tabla)
            input()
            
            # se limpia la lista para una nueva búsqueda
            del lista[:]
            lista[:] = []
            
            lista.append(tabla)

        else:
            os.system("cls")
            print ('GAME OVER')
            imprimir(tabla.tabla)
            input()
            break
            
    elif not len(lista) > 0:
        os.system("cls")
        print ('GAME OVER')
        imprimir(tabla.tabla)
        input()
        break
    elif ganoJ1(lista[0]):
        os.system("cls")
        print ('GANADOR: JUGADOR 1 (PC)')
        imprimir(tabla.tabla)
        input()
        break
    elif ganoJ2(lista[0]):
        os.system("cls")
        print ('GANADOR: JUGADOR 2 (TÚ)')
        imprimir(tabla.tabla)
        input()
        break
