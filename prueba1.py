# Esto es una prueba

class operacionesNumericas:

    def __init__(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2


    def sumar(self):
        
        return self.numero1 + self.numero2
    
    def imprimir_resultado():
        print(f"El resultado de la suma es {operacionesNumericas.sumar()}")


num1 = operacionesNumericas(5,6)
num1.imprimir_resultado()



        