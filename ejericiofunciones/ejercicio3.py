def ListaVacia(lista):
    print('\n\t---lista---\n')
    while True:
        valores=int(input('Digite los valores: '))
        if valores==0:
            print(f'Valores Numericos---> {lista}\nLongitud de la lista: {len(lista)}')
            break
        if len(lista)<10:
            valores not in lista
            lista.append(valores)
        else:
            print(f'\nLa longitud maxima es---> {len(lista)}\nsalir---> (0)')
lista=list()
ListaVacia(lista)