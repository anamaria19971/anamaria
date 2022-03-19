n1=int(input("digite el numero: "))
n2=int(input("digite el numero: "))
n3=int(input("digite el numero: "))

if n1>n2 and n2<n3:
    print(f"el numero menor es: {n2}")
elif n2>n1>n3:
    print(f"el numero menor es: {n3}")
elif n1<n2<n3:
    print(f"el numero menor es: {n1}")
else:
    print("solo hay numero iguales")