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


def validar_correo(correo):
    """
    Revisa que el correo tenga un formato básico: texto@dominio.ext
    Devuelve (True, "") si está bien, o (False, mensaje) si hay error.
    """
    correo = correo.strip()

    if " " in correo:
        return False, "El correo no debe tener espacios."
    if correo.count("@") != 1:
        return False, "El correo debe tener un solo @."
    usuario, dominio = correo.split("@")
    if usuario == "":
        return False, "Falta el texto antes del @."
    if "." not in dominio or dominio.startswith(".") or dominio.endswith("."):
        return False, "El dominio del correo no es válido (ejemplo: gmail.com)."
    return True, ""


def validar_telefono(telefono):
    """
    Revisa el celular: 9 dígitos, solo números, y que empiece con 9.
    Devuelve (True, "") si está bien, o (False, mensaje) si hay error.
    """
    telefono = telefono.strip()

    if not telefono.isdigit():
        return False, "El teléfono debe tener solo números."
    if len(telefono) != 9:
        return False, "El teléfono debe tener 9 dígitos."
    if telefono[0] != "9":
        return False, "El celular debe empezar con 9."
    return True, ""
