from auxiliares import *
from validaciones import *
from inputs import *
from textwrap import dedent
import random

def cargar_votos()->list:
    """
    Carga los datos de los votos en una matriz.
    Retorna una matriz de votos.
    
    Args:
        None
        
    Returns:
        matriz_votos (list): La matriz de votos.
    """
    matriz_votos = inicializar_matriz(pedir_cantidad_listas(),4)
    
    for lista in range(len(matriz_votos)):
        matriz_votos[lista][0] = pedir_lista()   
        for turno in range(1, len(matriz_votos[lista])):
            matriz_votos[lista][turno] = pedir_votos_por_turno(turno)
    
    return matriz_votos

def mostrar_resultados(matriz_votos:list)->None:
    """
    Recibe una matriz de votos e imprime los datos de cada lista.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        None
    """
      
    for lista in range(len(matriz_votos)):
        porcentaje_lista = calcular_porcentaje_votos_por_lista(matriz_votos, lista)
        print(f'LISTA NRO: {matriz_votos[lista][0]}')
        for turno in range(1, len(matriz_votos[lista])):
            print(f"VOTOS TURNO {mostrar_turno(turno).upper()}: {matriz_votos[lista][turno]} votos")
        print(f"PORCENTAJE DE VOTOS: {porcentaje_lista:.2f}%")
        print(f"{'-'* 40} ")
    return None

def ordenar_votos_por_turno(matriz_votos:list)->list:
    """
    Ordena de mayor a menor la matriz de votos por el turno elegido.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        matriz_votos (list): La matriz de votos ordenada.
    """
    
    print("¿Qué turno desea ordenar? \n")
    turno = pedir_turno()
    for i in range(len(matriz_votos)):
        for j in range(i+1, len(matriz_votos)):
            if matriz_votos[i][turno] < matriz_votos[j][turno]:
                aux = matriz_votos[i]
                matriz_votos[i] = matriz_votos[j]
                matriz_votos[j] = aux
    return matriz_votos

def mostrar_listas_menos_votadas(matriz_votos:list)->None:
    """
    Recibe una matriz de votos e 
    imprime las listas con menos del 5% de los votos.
    
    """
    print("Listas con menor porcentaje de votos (<5%): \n")
    listas_encontradas = False
    for lista in range(len(matriz_votos)):
        porcentaje_votos_lista = calcular_porcentaje_votos_por_lista(matriz_votos, lista)
        if porcentaje_votos_lista < 5:
            listas_encontradas = True
            print(dedent(f"""
            NRO LISTA: {matriz_votos[lista][0]}
            PORCENTAJE DE VOTOS: {porcentaje_votos_lista:.2f}%
            {'-'* 40}
                  """))
    if listas_encontradas == False:
        print("No se encontraron listas con menos del 5% de los votos.")
    return None

def mostrar_turno_con_mas_votos(matriz_votos:list)->None:
    """
    Imprime el turno con mas votos, en caso de empate,
    imprime los resultados de los turnos empatados.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        None
    """
    
    if verificar_empate(matriz_votos) == True:
        mostrar_empate(matriz_votos)
        return None
    else:
        turno_con_mas_votos = encontrar_turno_con_mas_votos(matriz_votos)
        nombre_turno_mas_votos = mostrar_turno(turno_con_mas_votos)
        votos_turno_con_mas_votos = sumar_votos_por_turno(matriz_votos, turno_con_mas_votos)

        print(dedent(f"""
        El turno con más votos es el turno {nombre_turno_mas_votos}, 
        con {votos_turno_con_mas_votos} votos."""))
        return None

def verificar_ballotage(matriz_votos:list)->bool:
    """
    Recibe una matriz de votos y verifica si se debe
    realizar una segunda vuelta.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        ballotage (bool): True si hay ballotage, False en caso contrario
    """
    
    ballotage = False    
    for lista in range(len(matriz_votos)):    
        if calcular_porcentaje_votos_por_lista(matriz_votos, lista) < 50:
            ballotage = True
        else:
            ballotage = False    
    if  ballotage == True:
        print("Hay ballotage.")
        return ballotage
    elif ballotage == False:
        print("No hay ballotage.")
        return ballotage

def realizar_segunda_vuelta(matriz_votos:list, ballotage:bool)->None:
    """
    Realiza la segunda vuelta electoral con los dos candidatos más votados.
    
    Si hay ballotage, se ordenan los resultados y se realizan los cálculos
    para determinar el ganador de la segunda vuelta.
    
    Si no hay ballotage, se muestra un mensaje y se finaliza.
    
    Parámetros:
        matriz_votos (list): Matriz de votos con los resultados de la primera vuelta.
        ballotage (bool): Indica si hay ballotage o no.
    
    Retorna:
        None
    """
    if ballotage == True:
        
        print("Realizando segunda vuelta...")
        ordenar_resultados(matriz_votos)
        
        primer_candidato = matriz_votos[0][0]
        segundo_candidato = matriz_votos[1][0]
        
        total_votos_segunda_vuelta = pedir_votos_segunda_vuelta()
        
        votos_primer_candidato = random.randint(0, total_votos_segunda_vuelta)
        votos_segundo_candidato = total_votos_segunda_vuelta - votos_primer_candidato
        
        matriz_ballotage = cargar_ballotage(primer_candidato, segundo_candidato, 
                                            votos_primer_candidato, votos_segundo_candidato)
        
        porcentaje_primer_candidato = calcular_porcentaje_votos_por_lista(matriz_ballotage, 0)
        porcentaje_segundo_candidato = calcular_porcentaje_votos_por_lista(matriz_ballotage, 1)
        
        
        
        if porcentaje_primer_candidato > porcentaje_segundo_candidato:
            mostrar_ganador(primer_candidato, votos_primer_candidato, porcentaje_primer_candidato)    
        elif porcentaje_segundo_candidato > porcentaje_primer_candidato:
            mostrar_ganador(segundo_candidato, votos_segundo_candidato, porcentaje_segundo_candidato)
        else:
            mostrar_empate(matriz_ballotage)
        return None


