año=int(input("digite el año"))
if año%4==0:
    print("el año es bisiesto")
if año%400==0 and año%100!=0:
    print("el año es bisiesto")
    print("el año no es bisiesto")
