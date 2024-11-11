def validar_cantidad_listas(cantidad_fil:any)->bool:
    """
    Recibe una cantidad de filas y retorna True si es válida, False en caso contrario.
    """
    bandera = True
    if len(cantidad_fil) == 0:
        bandera = False
    elif int(cantidad_fil) < 1 or int(cantidad_fil) > 5:
        bandera = False
    return bandera

def validar_lista(numero_lista:any)->bool:
    """
    Recibe un número de lista y retorna True si es válido, False en caso contrario.
    """
    bandera = True    
    if len(numero_lista) == 0:
        bandera = False
    elif int(numero_lista) < 100 or int(numero_lista) > 999:
        bandera = False
    return bandera

def validar_votos(votos:any)->bool:
    """
    Recibe una cantidad de votos y retorna True si es válida, False en caso contrario.
    """
    bandera = True
    if len(votos) == 0:
        bandera = False
    elif int(votos) < 0:
        bandera = False        
    return bandera   

def validar_turno(turno:any)->bool:
    """
    Recibe un numero de turno y retorna True si es valido, False en caso contrario.
    """
    bandera = True
    if len(turno) == 0:
        bandera = False
    elif int(turno) < 1 or int(turno) > 3:
        bandera = False
    return bandera

def validar_opcion(opcion:any)->bool:
    """
    Recibe una opcion y retorna True si es valida, False en caso contrario.
    """
    bandera = True
    if len(opcion) == 0:
        bandera = False
    elif int(opcion) < 1 or int(opcion) > 8:
        bandera = False
    return bandera
    
def validar_si_no(si_no:any)->bool:
    """
    Recibe una opcion (si/no) y retorna True si es valida, False en caso contrario.
    """
    bandera = True
    if len(si_no) == 0:
        bandera = False
    elif si_no != "s" and si_no != "n":
        bandera = False
    return bandera