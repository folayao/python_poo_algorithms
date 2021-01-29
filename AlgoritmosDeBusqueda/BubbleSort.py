import random

def ord_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j+1], lista[j]
    return lista

if __name__ == "__main__":
    tamanio_de_lista = int(input("Tamaño de la lista"))
    lista = [random.randint(0, 100) for i in range(tamanio_de_lista)]
    print(lista)
    lista_ordenada = ord_burbuja(lista)
    print(lista_ordenada)
