from validaciones import *
from auxiliares import *

def pedir_cantidad_listas()->int:
    """
    Pide la cantidad de listas que va a ingresar al sistema, 
    verifica que sea válida y la retorna.
    
    Args:
        None
        
    Returns:
        cantidad_fil (int): La cantidad de filas de la matriz.
    """
    
    cantidad_fil = input("Cantidad de listas que va a ingresar(máx 5): ")
    while validar_cantidad_listas(cantidad_fil) == False:
        print("Error.")
        cantidad_fil = input("Cantidad de listas que va a ingresar(máx 5): ")
    cantidad_fil = int(cantidad_fil)
    return cantidad_fil
        
def pedir_lista()->int:
    """
    Pide el número de la lista que va a ingresar al sistema, 
    verifica que sea válido y lo retorna.
    
    Args:
        None
        
    Returns:
        numero_lista (int): El número de la lista.
    """
    
    numero_lista = input("Ingrese un número de lista (3 cifras): ")
    while validar_lista(numero_lista) == False:
        print("Error.")
        numero_lista = input("Ingrese un número de lista (3 cifras): ")
    numero_lista = int(numero_lista)
    return numero_lista  
 
def pedir_votos_por_turno(turno:int)->int:
    """
    Pide la  cantidad de votos de cada turno, verifica que sea
    válida y la retorna.
    
    Args:
        turno (int): El turno del cual se ingresan los votos.
        
    Returns:
        votos (int): La cantidad de votos de ese turno.
    """
    
    votos = input(f"Ingrese los votos del turno {mostrar_turno(turno)}: ")
    while validar_votos(votos) == False:
        print("Error.")
        votos = input(f"Ingrese los votos del turno {mostrar_turno(turno)}: ")
    votos = int(votos)
    return votos

def pedir_turno()->int:
    """
    Pide un número de turno, lo verifica y lo retorna.
    
    Args:
        None
        
    Returns:
        turno (int): El número de turno ingresado.
    """
    turno = input("Ingrese el turno (1 = mañana, 2 = tarde, 3 = noche): ")
    while validar_turno(turno) == False:
        print("Error.")
        turno = input("Ingrese el turno (1 = mañana, 2 = tarde, 3 = noche): ")
    turno = int(turno)
    return turno

def pedir_votos_segunda_vuelta()->int:
    """
    Pide la  cantidad de votos de la segunda vuelta, verifica que sea
    válida y la retorna.
    
    Args:
        None
        
    Returns:
        votos_segunda_vuelta (int): La cantidad de votos de la segunda vuelta.
    """
    
    votos_segunda_vuelta = input("Ingrese los votos de la segunda vuelta: ")
    while validar_votos(votos_segunda_vuelta) == False:
        print("Error.")
        votos_segunda_vuelta = input("Ingrese los votos de la segunda vuelta: ")
    votos_segunda_vuelta = int(votos_segunda_vuelta)
    return votos_segunda_vuelta

def pedir_opcion(mensaje_input:str,mensaje_error:str)->int:
    """
    Pide un número de opción para el menú, lo verifica
    y lo retorna.
    
    Args:
        None
        
    Returns:
        opcion (int): El número ingresado.
    """
    opcion = input(mensaje_input)
    while validar_opcion(opcion) == False:
        print(mensaje_error)
        print(" ")
        opcion = input(mensaje_input)
    opcion = int(opcion)
    
    return opcion