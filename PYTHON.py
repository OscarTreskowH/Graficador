import numpy as np
import matplotlib.pyplot as plt
import os 

# Variables globales
x_min = None
x_max = None
x_range = None

def definir_dominio():
    global x_min, x_max, x_range
    try:
        x_min = float(input("Ingrese el valor mínimo de X: "))
        x_max = float(input("Ingrese el valor máximo de X: "))
        if x_min >= x_max:
            print("Error: xMin debe ser menor que xMax.")
            x_min = None
            x_max = None
        else:
            x_range = np.linspace(x_min, x_max, 100)
            print("|------------------------------------------------------------|")
            print(f"|****************************> Dominio definido de {x_min} a {x_max}.|")
            print("|------------------------------------------------------------|")            
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")

def funcion_triangular(a, b, c):
    if a >= b or b >= c:
        print("Error: Para la función triangular, A < B < C.")
        return None
    return np.maximum(0, np.minimum((x_range - a) / (b - a), (c - x_range) / (c - b)))

def funcion_trapezoidal(a, b, c, d):
    if a >= b or b >= c or c >= d:
        print("Error: Para la función trapezoidal, A < B < C < D.")
        return None
    return np.maximum(0, np.minimum(np.minimum((x_range - a) / (b - a), 1), (d - x_range) / (d - c)))

def funcion_gaussiana(c, sigma):
    return np.exp(-0.5 * ((x_range - c) / sigma) ** 2)


def funcion_campana(a, b, c):
    return 1 / (1 + np.abs((x_range - c) / a) ** (2 * b))


def graficar(funciones, nombres):
    if x_range is None:
        print("Error: Primero debe definir el dominio de X.")
        return
    plt.figure()
    for f, nombre in zip(funciones, nombres):
        if f is not None:
            plt.plot(x_range, f, label=nombre)
        else:
            print(f"Advertencia: La función {nombre} no está definida.")
    plt.legend()
    plt.show()

def menu():
    os.system("cls")
    F1, F2, F3, F4, F5, F6, F7, F8 = None, None, None, None, None, None, None, None
    while True:
        print("| ---------------------------------------------------------- |")  
        print("|******* (Evaluación N1 Oscar Treskow - Isaias Pino) ******* |")  
        print("|----------------------------------------------------------- |") 
        print("|                    Menu Principal:                         |")
        print("|----------------------------------------------------------- |") 
        print("|1.| Definir Dominio de X (xMin-xMax)                        |")
        print("|----------------------------------------------------------- |")         
        print("|2.| Definir dos funciones Triangulares: F1 y F2             |")
        print("|----------------------------------------------------------- |")         
        print("|3.| Definir dos funciones Trapezoidales: F3 y F4            |")
        print("|----------------------------------------------------------- |")         
        print("|4.| Definir dos funciones Gaussianas: F5 y F6               |")
        print("|----------------------------------------------------------- |")         
        print("|5.| Definir dos funciones Campana Generalizada: F7 y F8     |")
        print("|----------------------------------------------------------- |")         
        print("|6.| Graficar F1, F3, F5 y F6                                |")
        print("|----------------------------------------------------------- |")         
        print("|7.| Graficar F2, F4, F6 y F8                                |")
        print("|----------------------------------------------------------- |")         
        print("|8.| Graficar F1, F2, F5 y F6                                |")
        print("|----------------------------------------------------------- |")         
        print("|9.| Graficar F3, F4, F7 y F8                                |")
        print("|----------------------------------------------------------- |")         
        print("|10| Salir del Programa                                      |")
        print("|----------------------------------------------------------- |")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            definir_dominio()
        
        elif opcion == '2':
            if x_range is None:
                print("Error: Defina primero el dominio de X.")
            else:
                try:
                    a1, b1, c1 = map(float, input("Ingrese A, B, C para F1 (triangular): ").split())
                    a2, b2, c2 = map(float, input("Ingrese A, B, C para F2 (triangular): ").split())
                    F1 = funcion_triangular(a1, b1, c1)
                    F2 = funcion_triangular(a2, b2, c2)
                    print("Funciones triangulares definidas.")
                except ValueError:
                    print("Error: Asegúrese de ingresar valores numéricos para A, B, C.")
        
        elif opcion == '3':
            if x_range is None:
                print("Error: Defina primero el dominio de X.")
            else:
                try:
                    a3, b3, c3, d3 = map(float, input("Ingrese A, B, C, D para F3 (trapezoidal): ").split())
                    a4, b4, c4, d4 = map(float, input("Ingrese A, B, C, D para F4 (trapezoidal): ").split())
                    F3 = funcion_trapezoidal(a3, b3, c3, d3)
                    F4 = funcion_trapezoidal(a4, b4, c4, d4)
                    print("Funciones trapezoidales definidas.")
                except ValueError:
                    print("Error: Asegúrese de ingresar valores numéricos para A, B, C, D.")
        
        elif opcion == '4':
            if x_range is None:
                print("Error: Defina primero el dominio de X.")
            else:
                try:
                    c5, sigma5 = map(float, input("Ingrese C, sigma para F5 (gaussiana): ").split())
                    c6, sigma6 = map(float, input("Ingrese C, sigma para F6 (gaussiana): ").split())
                    F5 = funcion_gaussiana(c5, sigma5)
                    F6 = funcion_gaussiana(c6, sigma6)
                    print("Funciones gaussianas definidas.")
                except ValueError:
                    print("Error: Asegúrese de ingresar valores numéricos para C y sigma.")

        elif opcion == '5':
            if x_range is None:
                print("Error: Defina primero el dominio de X.")
            else:
                try:
                    a7, b7, c7 = map(float, input("Ingrese A, B, C para F7 (campana generalizada): ").split())
                    a8, b8, c8 = map(float, input("Ingrese A, B, C para F8 (campana generalizada): ").split())
                    F7 = funcion_campana(a7, b7, c7)
                    F8 = funcion_campana(a8, b8, c8)
                    print("Funciones campana generalizada definidas.")
                except ValueError:
                    print("Error: Asegúrese de ingresar valores numéricos para A, B, C.")
        
        elif opcion == '6':
            graficar([F1, F3, F5, F6], ['F1', 'F3', 'F5', 'F6'])

        elif opcion == '7':
            graficar([F2, F4, F6, F8], ['F2', 'F4', 'F6', 'F8'])

        elif opcion == '8':
            graficar([F1, F2, F5, F6], ['F1', 'F2', 'F5', 'F6'])

        elif opcion == '9':
            graficar([F3, F4, F7, F8], ['F3', 'F4', 'F7', 'F8'])

        elif opcion == '10':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
