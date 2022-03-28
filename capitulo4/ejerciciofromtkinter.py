from tkinter import E

edad=int(input("digite su edad: "))
peso=int(input("digite su peso: "))
latidos_corazon=int(input("digite sus latidos de corazon por minuto: "))
plaquetas=int(input("digite la cantidad normal de plaquetas: "))

if(edad>18) and (edad<65) and (peso>57) and (peso<82) and (latidos_corazon>60) and (latidos_corazon<100) and (plaquetas==150000):
    print("¡Apto! para donar sandre")
else:
    print("¡No! es apto para donar sandre")