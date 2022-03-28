contar=0
texto=input('ingrese palabra: ')
alfabeto='AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz'
for i in texto:
    if i in alfabeto:
        contar+=1
    else:
        print('no son alfabeticos')
if contar==len(texto):
    print('son alfabeticos')