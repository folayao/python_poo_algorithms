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

