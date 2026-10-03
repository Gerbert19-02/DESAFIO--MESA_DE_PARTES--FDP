# validaciones.py
# Funciones para revisar que los datos del expediente estén bien escritos.


def validar_documento(tipo, numero):
    """
    Revisa el documento de identidad.
    - DNI: 8 dígitos. RUC: 11 dígitos. Solo números.
    Devuelve (True, "") si está bien, o (False, mensaje) si hay error.
    """
    tipo = tipo.strip().upper()
    numero = numero.strip()

    if tipo != "DNI" and tipo != "RUC":
        return False, "El tipo de documento debe ser DNI o RUC."
    if not numero.isdigit():
        return False, "El número de documento debe tener solo números."
    if tipo == "DNI" and len(numero) != 8:
        return False, "El DNI debe tener 8 dígitos."
    if tipo == "RUC" and len(numero) != 11:
        return False, "El RUC debe tener 11 dígitos."
    return True, ""


def validar_folios(texto):
    """
    Revisa que los folios sean un número entero mayor a 0.
    Devuelve (True, "", folios) si está bien, o (False, mensaje, 0) si hay error.
    """
    texto = texto.strip()

    if not texto.isdigit():
        return False, "El número de folios debe ser un número entero.", 0
    folios = int(texto)
    if folios <= 0:
        return False, "El número de folios debe ser mayor a 0.", 0
    return True, "", folios