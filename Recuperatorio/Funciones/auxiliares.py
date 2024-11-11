from validaciones import *
from inputs import *
from textwrap import dedent
import os

def inicializar_matriz(cantidad_fil:int, cantidad_col:int)->list:
    """
    Recibe una cantidad de filas y columnas y retorna una
    matriz de ceros.
    
    Args: 
        cantidad_fil (int): La cantidad de filas de la matriz.
        cantidad_col (int): La cantidad de columnas de la matriz.
        
    Returns:
        matriz (list): La matriz inicializada.
    """
    
    matriz = []
    
    for i in range(cantidad_fil):  #recorro la cantidad de filas
        fila = [0] * cantidad_col  #creo una fila con la cantidad de columnas
        matriz += [fila]           #agrego la fila a la matriz
    return matriz

def mostrar_turno(num_turno:int)->str:
    """
    Recibe un numero de turno y retorna el nombre del turno.
    
    Args:
        num_turno (int): El turno a mostrar.
        
    Returns:
        turno (str): El nombre del turno.
    """
    
    turno = ""
    if num_turno == 1:
        turno = "manana"
    elif num_turno == 2:
        turno = "tarde"
    else:
        turno = "noche"
    return turno

def sumar_votos_por_lista(matriz_votos:list, lista:int)->int:
    """
    Recibe una matriz de votos y un número de lista.
    Retorna la suma de los votos de la lista especificada.
    
    Args:
        matriz_votos (list): La matriz de votos.
        lista (int): El número de la lista.
        
    Returns:
        votos_por_lista (int): La suma de los votos de la lista.
    """
    
    votos_por_lista = 0
    for turno in range(1, len(matriz_votos[lista])):  #recorro la cantidad de turnos
        votos_por_lista += matriz_votos[lista][turno] #sumo los votos de cada turno
    return votos_por_lista
    
def sumar_total_votos(matriz_votos:list)->int:
    """
    Recibe una matriz de votos y retorna la suma total de los votos.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        total_votos (int): La suma total de los votos.
    """
    
    total_votos = 0
    
    for lista in range (len(matriz_votos)):                             #recorro la cantidad de listas
            total_votos += sumar_votos_por_lista(matriz_votos, lista)   #sumo los votos de cada lista
    return total_votos    

def calcular_porcentaje_votos_por_lista(matriz_votos:list, lista:int)->int:
    """
    Recibe una matriz de votos y un número de lista.
    Calcula el porcentaje de votos de la lista.
    
    Args:
        matriz_votos (list): La matriz de votos.
        lista (int): El número de la lista.
        
    Returns:
        porcentaje_votos_lista (int): El porcentaje de votos de la lista.
    """

    votos_por_lista = 0                                             #inicializo las variables
    total_votos = 0
    porcentaje_votos_lista = 0
    
    votos_por_lista = sumar_votos_por_lista(matriz_votos, lista)    #sumo los votos de la lista
    total_votos = sumar_total_votos(matriz_votos)                   #sumo los votos totales
    
    porcentaje_votos_lista = votos_por_lista / total_votos * 100    #calculo el porcentaje
    
    return porcentaje_votos_lista

def sumar_votos_por_turno(matriz_votos:list, turno:int)->int:
    """
    Recibe una matriz de votos y un número de turno.
    Retorna la suma de los votos del turno especificado.
    
    Args:
        matriz_votos (list): La matriz de votos.
        turno (int): El número de turno.
        
    Returns:
        votos_por_turno (int): La suma de los votos del turno.
    """
    
    votos_por_turno = 0
    for lista in matriz_votos:              #recorro la cantidad de listas  
        votos_por_turno += lista[turno]     #sumo los votos de cada turno
    return votos_por_turno
        
def encontrar_turno_con_mas_votos(matriz_votos:list)->int:
    """
    Recibe una matriz de votos.
    Retorna el turno con mayor cantidad de votos.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        turno_con_mas_votos (int): El turno con mayor cantidad de votos.
    """
    
    votos_mañana = sumar_votos_por_turno(matriz_votos, 1)           #sumo los votos de cada turno
    votos_tarde = sumar_votos_por_turno(matriz_votos, 2)
    votos_noche = sumar_votos_por_turno(matriz_votos, 3)
    turno_con_mas_votos = None
    
    if votos_mañana > votos_tarde and votos_mañana > votos_noche:   #busco el turno con mas votos
        turno_con_mas_votos = 1
    elif votos_tarde > votos_mañana and votos_tarde > votos_noche:
        turno_con_mas_votos = 2
    elif votos_noche > votos_mañana and votos_noche > votos_tarde:
        turno_con_mas_votos = 3
    else:
        return None
    return turno_con_mas_votos

def verificar_empate(matriz_votos:list)->bool:
    """
    Recibe una matriz de votos.
    Retorna True si hay empate entre dos turnos.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        bandera_empate (bool): True si hay empate entre dos turnos.
    """
    
    bandera_empate = False
    turno_con_mas_votos = encontrar_turno_con_mas_votos(matriz_votos)   #busco el turno con mas votos
    if turno_con_mas_votos == None:                                     #si no hay turno con mas votos, hay empate
        bandera_empate = True
        return bandera_empate

def mostrar_empate(matriz_votos:list)->None:
    """
    Recibe una matriz de votos e imprime los turnos empatados.
    
    Args:
        matriz_votos (list): La matriz de votos.
    Returns:
        None
    """
    
    if verificar_empate(matriz_votos) == True:                  #si hay empate
        votos_mañana = sumar_votos_por_turno(matriz_votos, 1)   #sumo los votos de cada turno
        votos_tarde = sumar_votos_por_turno(matriz_votos, 2)
        votos_noche = sumar_votos_por_turno(matriz_votos, 3)
                                                                #imprimo los turnos empatados
        print(dedent(f"""                                       
        {'-'* 40}
        Hay un empate en el turno con más votos.
        Votos por turno:
        Turno mañana: {votos_mañana}
        Turno tarde: {votos_tarde}
        Turno noche: {votos_noche} 
        {'-'* 40}
        """))
        
        return None

def ordenar_resultados(matriz_votos:list)->list:
    """
    Recibe una matriz de votos y retorna la matriz ordenada
    de mayor a menor, según la cantidad de votos por lista.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        matriz_votos (list): La matriz de votos ordenada.
    """
    
    for lista in range(len(matriz_votos)):                      #recorro la cantidad de listas
        for turno in range(lista + 1, len(matriz_votos)):       #recorro la cantidad de turnos
            if sumar_votos_por_lista(matriz_votos, lista) < sumar_votos_por_lista(matriz_votos, turno): #comparo las cantidades de votos
                aux = matriz_votos[lista]                       #intercambio las listas
                matriz_votos[lista] = matriz_votos[turno]       
                matriz_votos[turno] = aux                       
    return matriz_votos

def cargar_ballotage(primer_candidato:str, segundo_candidato:str,
                     votos_primer_candidato:int, votos_segundo_candidato:int)->list:
    """
    Recibe las dos listas que participan en el ballotage y sus respectivos votos 
    y retorna una matriz con estos datos.
    
    Args:
        primer_candidato (str): Numero de lista del primer candidato.
        segundo_candidato (str): Numero de lista del segundo candidato.
        votos_primer_candidato (int): La cantidad de votos del primer candidato.
        votos_segundo_candidato (int): La cantidad de votos del segundo candidato.
        
    Returns:
        matriz_ballotage (list): La matriz con los datos del ballotage.
    """
    
    matriz_ballotage = [[primer_candidato, votos_primer_candidato],     #declaro la matriz
                        [segundo_candidato, votos_segundo_candidato]]
    
    return matriz_ballotage

def mostrar_ganador(lista:int, votos:int, porcentaje_de_votos:float)->None:
    """
    Recibe la lista ganadora, la cantidad de votos y el porcentaje de votos.
    Imprime los datos del ganador.
    
    Args:
        lista (int): La lista ganadora.
        votos (int): La cantidad de votos.
        porcentaje_de_votos (float): El porcentaje de votos.
        
    Returns:
        None
    """
    #imprimo los datos del ganador
    print(dedent(f"""      
    El ganador es la lista {lista} 
    con {votos} votos 
    y un porcentaje de {porcentaje_de_votos:.2f}%
    """))
    return None

def limpiar_consola()->None:
    """
    Limpia la consola una vez que se sale del sistema.
    
    Args:
        None
        
    Returns:
        None
    """
    
    print("Saliendo...")
    os.system('cls')
    return None

def salir_del_sistema()->None:
    """
    Pregunta al usuario si desea salir del sistema, en caso afirmativo limpia la consola,
    caso contrario no hace nada.
    
    Args:
        None
        
    Returns:
        None
    """
    salida = input("Esta seguro que desea salir del sistema? (s / n): ")        #pregunto al usuario si desea salir
    
    while validar_si_no(salida) == False: #valido la respuesta
        salida = input("Esta seguro que desea salir del sistema? (s / n): ") 
    if salida == "s": #si la respuesta es afirmativa, limpio la consola
        limpiar_consola()
        print("✦ GRACIAS POR USAR NUESTRO SISTEMA ✦")
        print(f"{'-'* 50} ")
        print(" ")
    else: #si la respuesta es negativa, no hago nada
        return None
    
def mostrar_menu()->None:
    """
    Muestra en pantalla el menu de opciones.
    
    Args:
        None
        
    Returns:
        None
    """
    #imprimo el menu
    print(dedent(
    """
    1. Cargar votos
    2. Mostrar resultados
    3. Ordenar votos por turno
    4. Mostrar las listas menos votadas
    5. Mostrar el turno con más votos
    6. Verificar si hay Ballotage
    7. Realizar segunda vuelta
    8. Salir

    """))
    return None
          


