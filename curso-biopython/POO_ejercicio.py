'''
El código presentado a continuación sirve para demostrar el uso de la Programación Orientada a Objetos (POO) en Python y aplicar los conocimientos vistos en clase.  
1. Define una clase base 'Animal' con atributos comunes como nombre y edad, y un método para hacer ruido. 
2. Luego se crean dos clases derivadas, 'Perro' y 'Gato', que heredan de 'Animal' y sobrescriben el método 'haz_ruido' para devolver sonidos específicos ('guau' para perros y 'miau' para gatos). 
3. La clase 'Gato' también incluye un atributo adicional 'usa_areno'. Finalmente, se crean objetos de ambas clases y se muestran sus atributos y los sonidos que hacen, demostrando herencia y polimorfismo en POO. 
'''

# Clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def haz_ruido(self):
        return "AAAAAAH"

# Clase Perro heredando de Animal
class Perro(Animal):
    def haz_ruido(self):
        return "guau"

# Clase Gato heredando de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, usa_areno=True):
        super().__init__(nombre, edad)
        self.usa_areno = usa_areno
    
    def haz_ruido(self):
        return "miau"

# Creación de objetos Perro y Gato
chilpi = Perro("chilpi", 8)
milky = Gato("milky", 10)

# Mostrar el ruido que hacen y sus atributos
print(chilpi.haz_ruido())  
print(chilpi.__dict__)    

print(milky.haz_ruido()) 
print(milky.__dict__)  





