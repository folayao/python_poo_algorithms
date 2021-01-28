class Persona(object):
    """docstring for Persona."""
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print(f'Yo {self.nombre} Ando Caminando')
        

class Ciclista(Persona):
    """docstring for Ciclista."""
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print(f'Yo {self.nombre} Ando moviendome en Bicicleta')
        
        
        
def main():
    ciclista = Ciclista('David')
    persona = Persona('Daniela')
    
    ciclista.avanza()
    persona.avanza()
    
if __name__ == '__main__':
    main()