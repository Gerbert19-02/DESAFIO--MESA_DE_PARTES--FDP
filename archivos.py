# archivos.py
# Funciones para guardar y cargar los expedientes en un archivo de texto.
# Cada expediente se guarda en una línea, con los datos separados por "|".

NOMBRE_ARCHIVO = "expedientes.txt"
POSICION_FOLIOS = 10  # lugar de la lista de folios dentro de "listas"


def guardar_expedientes(listas):
    """
    Guarda todos los expedientes en el archivo de texto.
    'listas' es el grupo de listas paralelas (código, fecha, tipo de persona...).
    Cada línea del archivo es un expediente.
    """
    cantidad = len(listas[0])
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
        for i in range(cantidad):
            datos = []
            for lista in listas:
                # Se cambia "|" por "/" para no romper el formato del archivo
                datos.append(str(lista[i]).replace("|", "/"))
            archivo.write("|".join(datos) + "\n")


def cargar_expedientes(listas):
    """
    Lee el archivo y llena las listas paralelas con los expedientes guardados.
    Si el archivo no existe todavía, no hace nada.
    Devuelve la cantidad de expedientes cargados.
    """
    cargados = 0
    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.rstrip("\n").split("|")
                if len(datos) != len(listas):
                    continue  # línea dañada: se ignora
                for i in range(len(listas)):
                    if i == POSICION_FOLIOS:
                        listas[i].append(int(datos[i]))
                    else:
                        listas[i].append(datos[i])
                cargados += 1
    except FileNotFoundError:
        pass
    return cargados