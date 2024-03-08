class Persona:
    def __init__(self, nombre):
        self.nombreP = nombre

    def saludar(self):
        print('Hola, soy ', self.nombreP)
    
    def saludaralmundo():
        print('Hola Mundo!')

if __name__ == '__main__':
    p1 = Persona('Pepito')
    p2 = Persona('Juanito')
   

    p1.saludar()
    p2.saludar()
    
    saludaralmundo()

