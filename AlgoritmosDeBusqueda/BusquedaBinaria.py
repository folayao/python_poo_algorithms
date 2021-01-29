import random


def busqueda_binaria(lista, comienzo, final, objetivo,iter_bin=0):
    iter_bin+=1
    if comienzo > final:
        return (False,iter_bin)

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True,iter_bin)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo,iter_bin=iter_bin)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo,iter_bin=iter_bin)

if __name__ == "__main__":
    tamanio_de_lista = int(input('De que tamaño sera la lista? : '))

    objetivo = int(input('Que numero quieres encontrar? : '))

    lista = sorted([random.randint(0, 100) for i in range(tamanio_de_lista)])
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(
        f'El elemento {objetivo} {"esta" if {encontrado} else "no esta"} en la lista ')
