# Tipos de datos abstractos, clases, Instancias

* En python todo es un objeto y tiene un tipo
  * Representacion de datos y formas de interactuar con ellos.
* Formas de interactuar con un objeto:
  * Creación
  * Manipulación
  * Destrucción
  
* Ventajas:
  * Descomposición
  * Abstracción
  * Encapsulación

~~~
class <nombre_de_la_clase> (<super_class>):

    def __init__(self, <params>):
        <expression>

    def <nombre_del_metodo>(self, <params>):
        <expression>

~~~

**Ejemplo**

~~~
# Definición
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

# Uso
david = Persona('David', 28)
Felipe = Persona('Felipe', 26)

david.saluda(Felipe)
'Hola Felipe, me llamo David'
~~~

## Instancias

* Mientras que la clase es un molde, a los objetos creados se les conoce como instancias
* Cuando se crea una instancia, se ejecuta el metodo ***"__ init__"***
* Todos los métodos de una clases reciben implicitamente como primer parametro ***self*** 
* Los atributs de clase nos permiten:
  * Representar datos
  * Procedimientos para interactuar con los mismos (metodos)
  * Mecanismos para esconder la representación interna
* Se accede a los atributos con la notacion de  punto.
* Puede tener atributos privados. Por convención comienza por **"_"**

# Decomposición

* Partir un problema en problemas mas pequeños
* Las clases permiten crear mayores abstracciones en forma de componentes
* Cada clase se encarga de una parte del problema y el programa se vuelve más facil de mantener

# Abstraccion
* Enfocarnos en la información relevante
* Separar la informacion central de los detalles secundarios
* Podemos utilizar variables y metodos ( Privados o publicos)

# Funciones: base de los decoradores

El concepto de decorador en Python es algo que podríamos ubicar en un nivel “intermedio” en el manejo del lenguaje, por lo que es buena idea que tengas una base sólida del lenguaje, sobre todo en cuanto a funciones, al momento de profundizar e implementarlos.

Los decoradores son una forma sencilla de llamar funciones de orden mayor, es decir, funciones que toman otra función cómo parámetro y/o retornan otra función como resultado. De esta forma un decorador añade capacidades a una función sin modificarla.

Un ejemplo de esto son las llantas de un automóvil si les colocas cadenas para la nieve: aún puede andar y además extiende su funcionalidad para conducirse en otros terrenos.

### Recordando sobre funciones
Antes de abordar el tema de decoradores haremos un pequeño repaso por las funciones, las cuales retornan un valor ante la entrada de un argumento.

Analicemos este sencillo ejemplo donde una función que multiplica un número que se eleva a la tercer potencia:
~~~
def elevar_cubo(numero):
	return numero * numero * numero
~~~
Si damos como argumento el número 3, entonces tendremos como salida el número 27 al ejecutar la función:
~~~
>>> elevar_cubo(3)
27
~~~
### Funciones cómo objetos de primera-clase
Otro concepto importante a tener en cuenta es que en Python las funciones son objetos de primera-clase, es decir, que pueden ser pasados y utilizados cómo argumentos al igual que cualquier otro objeto (strings, enteros, flotantes, listas, etc.).

Veamos un ejemplo donde definimos 3 diferentes funciones que utilizaremos de manera conjunta:
~~~
def presentarse(nombre):
	return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
	return f"¡Hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante):
	return funcion_entrante("David")
~~~

Las primeras dos funciones son obvias en su resultado, donde nos mostrarán un mensaje con el valor de la variable nombre. La tercer función puede ser más compleja de predecir ya que toma una función cómo entrada y veamos que pasa cuando colocamos una función cómo atributo:
~~~
>>> consume_funciones(presentarse)
'Me llamo David'

>>> consume_funciones(estudiemos_juntos)
'¡Hey David, aprendamos Python!'
~~~
Pongamos atención en cómo la función consume_funciones() se escribe con paréntesis para ser ejecutada, mientras que la función presentarse y estudiemos_juntos para solo hacer referencia a estas.

### Funciones anidadas
Al igual que los condicionales y bucles también puedes colocar funciones dentro de otra función.

Toma un minuto para analizar el siguiente código e inferir cual será el resultado de salida:
~~~
def funcion_mayor():
	print("Esta es una función mayor y su mensaje de salida.")

	def librerias():
		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

	def frameworks():
		print("Algunos frameworks de Python son: Django, Dash y Flask.")

	frameworks()
	librerias()
~~~
Si llamamos a la función funcion_mayor tendremos la siguiente salida:
~~~
>>> funcion_mayor()
Esta es una función mayor y su mensaje de salida.
Algunos frameworks de Python son: Django, Dash y Flask.
Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.
 ~~~
Debemos considerar que las funciones anidadas dentro de funcion_mayor no se ejecutan sino hasta que se llama esta primera, siendo muestra del scope o alcance de las funciones y si las llamamos obtendremos un error.
 

# Getters, Setters y decorator property

En este punto estamos comenzando a utilizar conceptos en Python que comienzan a ser más avanzados, por lo que es normal que puedan parecerte complejos o difíciles de asimilar, así que te animo a que los repases un par de veces.

Puedes tener la tranquilidad de que si bien, al inicio no los implementas en su totalidad, podrás seguir avanzando en el curso y poco a poco incorporarlos a tus proyectos donde lo más importante es que sepas que cuentas con estas herramientas.

Entendiendo el concepto de decorador
Antes de comenzar me gustaría que analices el siguiente código:
~~~
def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

def zumbido():
	print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido)
~~~
¿Qué pasará si llamamos a la función zumbido()? si logras determinar el resultado de salida o entenderlo con detalle, entonces podemos seguir adelante.

Lo que sucede es lo siguiente:
~~~
>>> zumbido()
Este es el último mensaje...
Buzzzzzz
Este es el primer mensaje ;)
~~~
Si no diste con el resultado no te preocupes, solo hay que analizarlo con detalle y el truco está en la línea zumbido = funcion_decoradora(zumbido). Sucede que la función wrapper() recibió la la función zumbido() cómo parámetro y coloca su salida entre los otros dos prints.

Todo lo que sucede se conoce en programación como metaprogramación (metaprogramming), ya que una parte del programa trata de modificar a otra durante el tiempo de compilación. En tanto un decorador básicamente toma una función, le añade alguna funcionalidad y la retorna.

### Mejorando la sintaxis
Definitivamente la forma en que decoramos la función es complejo, pero afortunadamente Python lo tiene en cuenta y podemos utilizar decoradores con el símbolo @. Volviendo al mismo ejemplo de funcion_decoradora(), podemos simplificarlo así:
~~~
@funcion_decoradora
def zumbido():
	print("Buzzzzzz")
~~~
En solo tres líneas de código tenemos el mismo resultado que escribir zumbido = funcion_decoradora(zumbido).

### ¿Qué son getters y setters?
A diferencia de otros lenguajes de programación, en Python los getters y setters tienen el objetivo de asegurar el encapsulamiento de datos. Cómo habrás visto, si declaramos una variable privada en Python al colocar un guión bajo al inicio de esta (_) y normalmente son utilizados para: añadir lógica de validación al momento de obtener y definir un valor y, para evitar el acceso directo al campo de una clase.

La realidad es que en Python no existen variables netamente privadas, pues aunque se declaren con un guión bajo podemos seguir accediendo a estas. En Programación Orientada a Objetos esto es peligroso, pues podemos alterar el método de alguna clase y tener efectos colaterales que afecten la lógica de nuestra aplicación.

### Clases sin getters y setters
Veamos un ejemplo con una clase que almacena un dato de distancia recorrida en millas (mi) y lo convierte a kilómetros (km):
~~~
class Millas:
	def __init__(self, distancia = 0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)
~~~
Ahora creemos un objeto que haga referencia a un viaje:
~~~
# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos el atributo distancia
>>> print(avion.distancia)
200

# Obtenemos el método convertir_a_kilometros
>>> print(avion.convertir_a_kilometros())
321.8688
~~~
### Utilizando getters y setters
Incluyamos un par de métodos para obtener la distancia y otro para que no acepte valores inferiores a cero, pues no tendría sentido que un vehículo recorra una distancia negativa. Estos son métodos getters y setters:
~~~
class Millas:
	def __init__(self, distancia = 0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)

	# Método getter
	def obtener_distancia(self):
		return self._distancia

	# Método setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		self._distancia = valor
~~~
El método getter obtendrá el valor de la distancia que y el método setter se encargará de añadir una restricción. También debemos notar cómo distancia fue reemplazado por _distancia, denotando que es una variable privada.

Si probamos nuestro código funcionará, la desventaja es que cualquier aplicación que hayamos creado con una base similar deberá ser actualizado. Esto no es nada escalable si tenemos cientos o miles de líneas de código.

### Función *property()*
Esta función está incluida en Python, en particular crea y retorna la propiedad de un objeto. La propiedad de un objeto posee los métodos getter(), setter() y del().

En tanto la función tiene cuatro atributos: property(fget, fset, fsel, fdoc) :

fget : trae el valor de un atributo.
fset : define el valor de un atributo.
fdel : elimina el valor de un atributo.
fdoc : crea un docstring por atributo.
Veamos un ejemplo del mismo caso implementando la función property() :
~~~
class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	def definir_distancia(self, recorrido):
		print("Llamada al método setter")
		self._distancia = recorrido

	# Función para eliminar el atributo _distancia
	def eliminar_distancia(self):
		del self._distancia

	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

# Creamos un nuevo objeto 
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
>>> print(avion.distancia)
Llamada al método getter
Llamada al método setter
200
~~~
Aunque en este ejemplo hay una sola llamada a print, tenemos tres líneas como salida pues esta llama a los primeros dos métodos. Por lo que la propiedad distancia es una propiedad de objeto que ayuda a mantener el acceso de forma privada.

### Decorador *@property*
Este decorador es uno de varios con los que ya cuenta Python, el cual nos permite utilizar getters y setters para hacer más fácil la implementación de la programación orientada a objetos en Python cambiando los métodos o atributos de las clases de forma que no modifiquemos el código.

Pero mejor veamos un ejemplo en acción:
~~~
class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter
	def definir_distancia(self, valor)
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self._distancia = valor

# Creamos un nuevo objeto 
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
>>> print(avion.distancia)
Llamada al método getter
Llamada al método setter
200
~~~
De esta manera usamos el decorador @property para utilizar getters y setters de una forma más prolija e incluimos una nueva funcionalidad a nuestro método definir_distancia() , al mismo tiempo protegemos el acceso a nuestras variables privadas y cumplimos con el principio de encapsulación.

# Encapsulación

* Permite agrupar datos y su comportamiento
* controla el acceso a dichos datos
* Previene modificaciones no autorizadas.

~~~
class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista')


casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
print(casilla.region)
casilla.region = 'Mexico'
print(casilla.region)
~~~

# Herencia


* Permite modelar una jerarquia de clases
* Permiter compartir comportamiento comun en la jerarquia 
* Al pradre sele conoce como super clase y al hijo como sub-clase

# Polimorfismos

* La habilidad de tomar varias formas
* En Python, Nos permite cambiar el comportamiento de  una super clase para adaptarlo a la subclase 

