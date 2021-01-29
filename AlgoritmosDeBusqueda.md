# Busqueda Lineal

* Busca en todos los elementos de manera secuencial.
* ¿Cual es el peor caso?

~~~
import random

def busqueda_lineal(lista, objetivo):
    match = False
    
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match



if __name__ == "__main__":
    tamanio_de_lista = int(input('De que tamaño sera la lista? : '))
    
    objetivo = int(input('Que numero quieres encontrar? : '))
    
    lista = [random.randint(0,100) for i in range(tamanio_de_lista)]
    encontrado  = busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if {encontrado} else "no esta"} en la lista ')
~~~

# Busqueda Binaria

* Divide y conquista
* el problema se divine en 2 en cada iteracion
* ¿Cual es el peor caso?


# Ordenamiento Burbuja

Es un algoritmo que repite repetidamente una lista que necesita ordenarse. Compara elementos adyacentes y los intercambia si estan en el orden incorrecto. este procedimiento se repite hasta que no se requieren mas intercambios , lo que indica que la lista se encuentra ordenada

# Merge Sort

Divide y conquista

El ordenamiento por mezcla es un algoritmo que divide y conquista. Primero divide una lista en partes iguales hasta que queden sublistas de 1 a 0 elementos. luego las recombina de forma ordenada.

