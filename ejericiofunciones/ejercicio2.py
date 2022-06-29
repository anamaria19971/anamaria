# funcion
def marcas(elementos, cadena, ordenar):
    print('\n\t---Contenido de la lista---\n')
    contador = 1
    for i in elementos:
        print(f'{contador}. {i}')
        contador += 1
        print(f'\n\t---Cadena de caracter---')
        contador = 1
        for x in ordenar:
            print('f {contador}, {x}')
            contador += 1


# programa principal
elementos = ['Samsung', 'Motorola', 'Huawei', 'Apple',
            'Xiomi', 'LG', 'Lenovo', 'Nokia', 'Oppo', 'Htc']
cadena = ",".join(elementos)
ordenar = sorted(elementos)
marcas(elementos, cadena, ordenar)
# funcion


def marcas(longitud):
    while True:
        buscar = str(
            input('\n digite la marca del celular que desea buscar : '))
        if buscar == 'x':
            print(':)')
            break
        if buscar in elementos:
            print(f'\n\t---Resultado---\n\n{buscar}')
        else:
            print('marca no existente en el sistema')
    print(longitud)


# programa principal
longitud = len(elementos)
marcas(longitud)