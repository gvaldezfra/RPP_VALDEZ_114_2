from auxiliares import *
from principales import * 
from inputs import * 
from validaciones import *
import os


def ejecutar_menu()->None:
    """
    Permite al usuario ingresar al sistema de votación.
    
    Args:
        None
        
    Returns:
        None
    """
    
    matriz_votos = []
    ballotage = False
    mensaje_input = "Ingrese su opción: "
    mensaje_error_1 = "Opcion no valida, ingrese nuevamente su opción: "
    mensaje_error_2 = "Primero debe cargar los votos (Opción 1)."
    mensaje_error_3 = "Primero debe verificar si hay Ballotage (Opción 6)."
    
    print("✦ BIENVENIDO AL SISTEMA DE VOTACIÓN ✦")
    while (True):
        
        mostrar_menu()
    
        opcion = pedir_opcion(mensaje_input,mensaje_error_1)
        
        if opcion == 1:
            matriz_votos = cargar_votos()
            print("Votos cargados con éxito.")
        
        elif opcion == 2:
            if matriz_votos:
                mostrar_resultados(matriz_votos)
            else:
                print(mensaje_error_2, end=f"\n{'-'*40}")
        
        elif opcion == 3:
            if matriz_votos:
                matriz_votos = ordenar_votos_por_turno(matriz_votos)
                print(" ")
                print("Votos ordenados con éxito.", end=" ")
            else:
                print(mensaje_error_2, end=f"\n{'-'*40}")
        
        elif opcion == 4:
            if matriz_votos:
                mostrar_listas_menos_votadas(matriz_votos)
            else:
                print(mensaje_error_2, end=f"\n{'-'*40}")
                
        elif opcion == 5:
            if matriz_votos:
                mostrar_turno_con_mas_votos(matriz_votos)
            else:
                print(mensaje_error_2, end=f"\n{'-'*40}")
        
        elif opcion == 6:
            if matriz_votos:
                ballotage = verificar_ballotage(matriz_votos)
                print("Verificación realizada con éxito.", end=" ")
            else:
                print(mensaje_error_2, end=f"\n{'-'*40}")
        
        elif opcion == 7:
            if ballotage:
                realizar_segunda_vuelta(matriz_votos, ballotage)
                print("Segunda vuelta realizada con éxito.", end=" ")
            else:
                print(mensaje_error_3, end=f"\n{'-'*40}")
                
        elif opcion == 8:
            salir_del_sistema()
            

def main():
    ejecutar_menu()

main()