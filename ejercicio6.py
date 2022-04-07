Meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
v_i=[]
for i in Meses:
    Valores=int(input("ingrese los valores de la produccion de cafe: "))
    v_i.append(Valores)
    Promedio=sum(v_i)/len(Meses)
print(F"{Meses}\n{v_i}\n promedio de produccion en el año: {Promedio}")
