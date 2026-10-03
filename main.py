# main.py
# Prototipo: Mesa de Partes Digital
# Curso: Fundamentos de Programación (CIIN1205P)

from datetime import datetime
from validaciones import validar_documento, validar_folios
from archivos import guardar_expedientes, cargar_expedientes

# ---------------------------------------------------------------------------
# ARREGLOS PARALELOS: una lista por dato; la misma posición = mismo expediente
# ---------------------------------------------------------------------------
lista_codigos = []
lista_fechas = []
lista_tipos_persona = []
lista_tipos_doc_identidad = []
lista_nums_doc_identidad = []
lista_nombres = []
lista_correos = []
lista_telefonos = []
lista_tipos_doc_tramite = []
lista_asuntos = []
lista_num_folios = []        # posición 10 (debe coincidir con archivos.py)
lista_areas_destino = []
lista_estados = []

TODAS_LAS_LISTAS = [
    lista_codigos, lista_fechas, lista_tipos_persona,
    lista_tipos_doc_identidad, lista_nums_doc_identidad, lista_nombres,
    lista_correos, lista_telefonos, lista_tipos_doc_tramite,
    lista_asuntos, lista_num_folios, lista_areas_destino, lista_estados,
]


def generar_codigo(cantidad_actual):
    """Crea el código único: EXP-2026-0001, EXP-2026-0002..."""
    return "EXP-2026-" + str(cantidad_actual + 1).zfill(4)


def registrar_expediente():
    """Pide los datos, los valida, genera el código y guarda en el archivo."""
    print("\n--- REGISTRO DE EXPEDIENTE ---")
    tipo_persona = input("Tipo de persona (NATURAL / JURIDICA): ").strip().upper()
    tipo_doc = input("Tipo de documento (DNI / RUC): ").strip().upper()
    num_doc = input("Número de documento: ").strip()
    nombre = input("Nombres y apellidos / Razón social: ").strip()
    correo = input("Correo electrónico: ").strip()
    telefono = input("Teléfono / Celular: ").strip()
    tipo_tramite = input("Tipo de trámite (SOLICITUD / OFICIO / CARTA): ").strip().upper()
    asunto = input("Asunto del trámite: ").strip()
    folios_texto = input("Número de folios: ")
    area = input("Área de destino: ").strip()

    # Validaciones (módulo validaciones.py)
    ok, mensaje = validar_documento(tipo_doc, num_doc)
    if not ok:
        print("[ERROR]", mensaje)
        return
    ok, mensaje, folios = validar_folios(folios_texto)
    if not ok:
        print("[ERROR]", mensaje)
        return

    # Código y fecha
    codigo = generar_codigo(len(lista_codigos))
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Guardar en los arreglos paralelos
    lista_codigos.append(codigo)
    lista_fechas.append(fecha)
    lista_tipos_persona.append(tipo_persona)
    lista_tipos_doc_identidad.append(tipo_doc)
    lista_nums_doc_identidad.append(num_doc)
    lista_nombres.append(nombre)
    lista_correos.append(correo)
    lista_telefonos.append(telefono)
    lista_tipos_doc_tramite.append(tipo_tramite)
    lista_asuntos.append(asunto)
    lista_num_folios.append(folios)
    lista_areas_destino.append(area)
    lista_estados.append("Registrado - En proceso")

    # Guardar en el archivo (módulo archivos.py)
    guardar_expedientes(TODAS_LAS_LISTAS)

    print("\n====== CARGO DIGITAL DE RECEPCIÓN ======")
    print("Código :", codigo)
    print("Fecha  :", fecha)
    print("Estado :", "Registrado - En proceso")
    print("Nombre :", nombre)
    print("Asunto :", asunto)
    print("Folios :", folios)
    print("Destino:", area)
    print("========================================")


def buscar_expediente():
    """Busca un expediente por código (búsqueda lineal)."""
    if len(lista_codigos) == 0:
        print("\n[AVISO] No hay expedientes registrados.")
        return

    codigo = input("\nIngrese el código del expediente (ej. EXP-2026-0001): ").strip().upper()
    encontrado = False
    for i in range(len(lista_codigos)):
        if lista_codigos[i] == codigo:
            print("\n--- EXPEDIENTE ENCONTRADO ---")
            print("Código   :", lista_codigos[i])
            print("Fecha    :", lista_fechas[i])
            print("Nombre   :", lista_nombres[i])
            print("Documento:", lista_tipos_doc_identidad[i], "-", lista_nums_doc_identidad[i])
            print("Asunto   :", lista_asuntos[i])
            print("Folios   :", lista_num_folios[i])
            print("Destino  :", lista_areas_destino[i])
            print("Estado   :", lista_estados[i])
            encontrado = True
            break

    if not encontrado:
        print("\n[INFO] No se encontró ningún expediente con ese código.")


def mostrar_lista():
    """Muestra todos los expedientes en una tabla."""
    print("\nCÓDIGO         | DOCUMENTO   | NOMBRE               | FOLIOS | ESTADO")
    print("-" * 80)
    for i in range(len(lista_codigos)):
        print(lista_codigos[i].ljust(14) + " | "
              + lista_nums_doc_identidad[i].ljust(11) + " | "
              + lista_nombres[i][:20].ljust(20) + " | "
              + str(lista_num_folios[i]).rjust(6) + " | "
              + lista_estados[i])


def ordenar_expedientes():
    """Ordena los expedientes por código (burbuja) y los muestra."""
    n = len(lista_codigos)
    if n < 2:
        print("\n[AVISO] Se necesitan al menos 2 expedientes para ordenar.")
        return

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista_codigos[j] > lista_codigos[j + 1]:
                # Se intercambia la misma posición en TODAS las listas
                for lista in TODAS_LAS_LISTAS:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    guardar_expedientes(TODAS_LAS_LISTAS)
    print("\n[ÉXITO] Expedientes ordenados por código.")
    mostrar_lista()


def menu_principal():
    """Muestra el menú y llama a la función elegida hasta que el usuario salga."""
    cargados = cargar_expedientes(TODAS_LAS_LISTAS)
    print("\nExpedientes cargados desde el archivo:", cargados)

    opcion = ""
    while opcion != "4":
        print("\n=== MESA DE PARTES DIGITAL ===")
        print("1) Registrar expediente")
        print("2) Buscar expediente por código")
        print("3) Ordenar expedientes por código")
        print("4) Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_expediente()
        elif opcion == "2":
            buscar_expediente()
        elif opcion == "3":
            ordenar_expedientes()
        elif opcion == "4":
            print("\nSaliendo del sistema...")
        else:
            print("\n[ERROR] Opción inválida.")


if __name__ == "__main__":
    menu_principal()