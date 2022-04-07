from multiprocessing.connection import Listener
from turtle import listen

list=int(input("digite tamaño de la lista que desea capturar"))
numeritos=[]
i=0
while i <=list :
    numero=int(input("digite el numero :"))
    numeritos.append(numero)
    i+=1
    for index, value in enumerate(numeritos):
        if (value < 1):
            numeritos[index] = 0
        print (value)