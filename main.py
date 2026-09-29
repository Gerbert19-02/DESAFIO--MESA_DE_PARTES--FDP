# %%
# ===============================================================================
# PROTOTIPO: MESA DE PARTES DIGITAL - MUNICIPALIDAD DISTRITAL DE LOS OLIVOS
# CURSO: FUNDAMENTOS DE PROGRAMACIÓN
# ===============================================================================

# ------------------------------------------------------------------------------
# TEMA 3: ARREGLOS PARALELOS (Nuestras "Cajitas de Memoria")
# Usamos una lista independiente para cada dato de tus entradas originales.
# Todas comparten la misma posición (índice 0, 1, 2...) para un mismo expediente.
# ------------------------------------------------------------------------------
lista_codigos = []
lista_fechas = []
lista_tipos_persona = []
lista_tipos_doc_identidad = []
lista_nums_doc_identidad = []
lista_nombres_completo = []
lista_correos = []
lista_telefonos = []
lista_tipos_doc_tramite = []
lista_asuntos = []
lista_num_folios = []
lista_areas_destino = []
lista_estados = []

# Contador que genera el código correlativo (Ej. Ex-2026-0001, Ex-2026-0002...)
contador_correlativo = 1

# ------------------------------------------------------------------------------
# TEMA 2: FUNCIONES Y MODULARIDAD
# ------------------------------------------------------------------------------

def registrar_expediente():
    """
    EXPLICACIÓN(REGISTRO):
    1. Pide todos tus campos originales por consola.
    2. Revisa que el documento sea DNI o RUC.
    3. Convierte los folios a número entero y verifica que sea mayor a 0.
    4. Si todo está bien, guarda el expediente al final de cada cajita (lista).
    """
    global contador_correlativo
    
    print("\n======================================================================")
    print("       MESA DE PARTES DIGITAL - REGISTRO DE EXPEDIENTE               ")
    print("======================================================================")
    
    # 1. ENTRADA DE DATOS (Tus variables originales)
    print("--- DATOS DEL ADMINISTRADO ---")
    tipo_persona = input("tipo de persona(NATURAL / JURIDICA):")
    tipo_doc_identidad = input("Tipo de documento (DNI /RUC):")
    num_doc_identidad = input("Número de docuento de identidad:")
    nombres_completo = input("Nombres y apellidos / Razón Social:")
    correo_electronico = input("Correo electrónico de contacto:")
    telefono_contacto = input("Teléfono / Celular de Contacto:")

    print("\n--- DATOS DEL TRAMITE DOCUMENTARIO ---")
    tipo_documento_tramite = input("Tipo de documento (SOLICITUD / OFICIO/ CARTA):")
    asunto_tramite = input("Asunto o sumilla del trámite:")
    num_folios_texto = input("Numero de folios presentados:")
    area_destino = input(" Area de destino (Ej. LINCENCIAS / TRÁMITE / ALCALDIA):")

    # 2. PROCESO (Validaciones)
    es_valido = True
    mensaje_error = ""

    # Validar el tipo de documento
    if tipo_doc_identidad == "DNI" or tipo_doc_identidad == "dni":
        es_valido = True
    elif tipo_doc_identidad == "RUC" or tipo_doc_identidad == "ruc":
        es_valido = True
    else:
        es_valido = False
        mensaje_error = "El tipo de documento de identidad debe ser DNI o RUC."

    # Validar los folios
    if es_valido:
        if num_folios_texto.isdigit():
            num_folios = int(num_folios_texto)
            if num_folios <= 0:
                es_valido = False
                mensaje_error = "El número de folios debe ser mayor a 0."
        else:
            es_valido = False
            mensaje_error = "El número de folios debe ser un valor entero numérico."

    # 3. SALIDA Y ALMACENAMIENTO EN LISTAS
    print("\n=====================================================================")
    if es_valido:
        codigo_expediente = "Ex-2026-" + str(contador_correlativo).zfill(4)
        fecha_registro = "18/09/2026 23:15:45"
        
        # Guardamos en las listas
        lista_codigos.append(codigo_expediente)
        lista_fechas.append(fecha_registro)
        lista_tipos_persona.append(tipo_persona)
        lista_tipos_doc_identidad.append(tipo_doc_identidad)
        lista_nums_doc_identidad.append(num_doc_identidad)
        lista_nombres_completo.append(nombres_completo)
        lista_correos.append(correo_electronico)
        lista_telefonos.append(telefono_contacto)
        lista_tipos_doc_tramite.append(tipo_documento_tramite)
        lista_asuntos.append(asunto_tramite)
        lista_num_folios.append(num_folios)
        lista_areas_destino.append(area_destino)
        lista_estados.append("REGISTRADO / EN PROCESO")
        
        contador_correlativo += 1

        print("              CÓDIGO DIGITAL DE RECEPCIÓN - MESA DE PARTES         ")
        print("===================================================================")
        print(" CÓDIGO DE EXPEDIENTE :", codigo_expediente)
        print(" FECHA DE RECEPCIÓN   :", fecha_registro)
        print(" ESTADO               :", "REGISTRADO / EN PROCESO")
        print("-------------------------------------------------------------------")
        print(" Administrado        :", nombres_completo)
        print(" Tipo Persona        :", tipo_persona)
        print(" Documento           :", tipo_doc_identidad, "-", num_doc_identidad)
        print(" Correo Electrónico   :", correo_electronico)
        print(" Teléfono             :", telefono_contacto)
        print("----------------------------------------------------------------------")
        print(" Tipo Documento       :", tipo_documento_tramite)
        print(" Asunto               :", asunto_tramite)
        print(" Folios               :", num_folios)
        print(" Área Destinataria    :", area_destino)
        print("----------------------------------------------------------------------")
        print(" [✓] Documento recibido de acuerdo con la Ley N.° 31170.")
        print(" Conserve este cargo digital para consultar el estado de su trámite.")
    else:
        print("                 ERROR EN EL REGISTRO DEL EXPEDIENTE                  ")
        print("======================================================================")
        print(" [X] No se pudo registrar el expediente.")
        print(" Motivo:", mensaje_error)
        print(" Por favor, verifique los datos ingresados e intente nuevamente.")

    print("======================================================================")

def listar_expedientes():
    """
    EXPLICACIÓN (RECORRIDO DE LISTAS):
    Abre nuestro 'archivador digital' y muestra en formato de tabla
    todos los expedientes guardados hasta el momento.
    """
    if len(lista_codigos) == 0:
        print("\n[AVISO]: No hay expedientes registrados en el sistema.")
        return

    print("\n=========================================================================================")
    print("                        LISTADO GENERAL DE EXPEDIENTES REGISTRADOS                       ")
    print("=========================================================================================")
    print("CÓDIGO         | DOC ID         | ADMINISTRADO           | FOLIOS | ÁREA DESTINO")
    print("-----------------------------------------------------------------------------------------")
    for i in range(len(lista_codigos)):
        print(lista_codigos[i] + " | " + lista_nums_doc_identidad[i] + " | " + lista_nombres_completo[i][:20].ljust(22) + " | " + str(lista_num_folios[i]).zfill(2) + "     | " + lista_areas_destino[i])
    print("=========================================================================================")

def buscar_expediente():
    """
    EXPLICACIÓN (BÚSQUEDA LINEAL):
    Funciona como buscar un libro en un estante: revisa uno por uno desde el primero
    hasta el último comparando si el código o el DNI/RUC coincide con lo que pidió el usuario.
    """
    if len(lista_codigos) == 0:
        print("\n[AVISO]: No hay expedientes registrados para realizar búsquedas.")
        return

    criterio = input("\nIngrese Código de Expediente (ej. Ex-2026-0001) o N° de Documento: ")
    encontrado = False

    for i in range(len(lista_codigos)):
        if lista_codigos[i] == criterio or lista_nums_doc_identidad[i] == criterio:
            print("\n-----------------------------------------------------")
            print("         EXPEDIENTE ENCONTRADO EN SISTEMA            ")
            print("-----------------------------------------------------")
            print("Código Expediente :", lista_codigos[i])
            print("Fecha Registro    :", lista_fechas[i])
            print("Administrado      :", lista_nombres_completo[i])
            print("Documento         :", lista_tipos_doc_identidad[i], "-", lista_nums_doc_identidad[i])
            print("Asunto            :", lista_asuntos[i])
            print("Folios            :", lista_num_folios[i])
            print("Área Destino      :", lista_areas_destino[i])
            print("Estado Actual     :", lista_estados[i])
            print("-----------------------------------------------------")
            encontrado = True
            break

    if not encontrado:
        print("\n[INFO]: No se encontró ningún expediente con el criterio ingresado.")

def ordenar_por_folios_burbuja():
    """
    EXPLICACIÓN(MÉTODO BURBUJA):
    Compara expedientes vecinos en las listas. Si el de la derecha tiene más folios
    que el de la izquierda, los intercambia de posición como si fuera una burbuja subiendo.
    Intercambia la posición en TODAS las listas para que los datos del expediente no se mezclen.
    """
    n = len(lista_num_folios)
    if n <= 1:
        print("\n[AVISO]: Se requieren al menos 2 expedientes para ordenar.")
        return

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista_num_folios[j] < lista_num_folios[j + 1]:
                # Intercambio simultáneo en las 13 listas paralelas
                lista_num_folios[j], lista_num_folios[j + 1] = lista_num_folios[j + 1], lista_num_folios[j]
                lista_codigos[j], lista_codigos[j + 1] = lista_codigos[j + 1], lista_codigos[j]
                lista_fechas[j], lista_fechas[j + 1] = lista_fechas[j + 1], lista_fechas[j]
                lista_tipos_persona[j], lista_tipos_persona[j + 1] = lista_tipos_persona[j + 1], lista_tipos_persona[j]
                lista_tipos_doc_identidad[j], lista_tipos_doc_identidad[j + 1] = lista_tipos_doc_identidad[j + 1], lista_tipos_doc_identidad[j]
                lista_nums_doc_identidad[j], lista_nums_doc_identidad[j + 1] = lista_nums_doc_identidad[j + 1], lista_nums_doc_identidad[j]
                lista_nombres_completo[j], lista_nombres_completo[j + 1] = lista_nombres_completo[j + 1], lista_nombres_completo[j]
                lista_correos[j], lista_correos[j + 1] = lista_correos[j + 1], lista_correos[j]
                lista_telefonos[j], lista_telefonos[j + 1] = lista_telefonos[j + 1], lista_telefonos[j]
                lista_tipos_doc_tramite[j], lista_tipos_doc_tramite[j + 1] = lista_tipos_doc_tramite[j + 1], lista_tipos_doc_tramite[j]
                lista_asuntos[j], lista_asuntos[j + 1] = lista_asuntos[j + 1], lista_asuntos[j]
                lista_areas_destino[j], lista_areas_destino[j + 1] = lista_areas_destino[j + 1], lista_areas_destino[j]
                lista_estados[j], lista_estados[j + 1] = lista_estados[j + 1], lista_estados[j]

    print("\n[ÉXITO]: Expedientes ordenados por cantidad de folios (de mayor a menor).")
    listar_expedientes()

# ------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL (Menú Interactivo)
# ------------------------------------------------------------------------------
def menu_principal():
    """
    EXPLICACIÓN (MENÚ PRINCIPAL):
    Es el tablero de control del sistema. Mantiene la consola encendida mediante un
    bucle 'while' hasta que el usuario elija la opción '5' (Salir).
    """
    opcion = ""
    while opcion != "5":
        print("\n======================================================================")
        print("   MESA DE PARTES DIGITAL - MUNICIPALIDAD DISTRITAL DE LOS OLIVOS    ")
        print("======================================================================")
        print("1. Registrar nuevo expediente")
        print("2. Listar expedientes registrados")
        print("3. Buscar expediente (por Código o N° Documento)")
        print("4. Ordenar expedientes por folios (Método Burbuja)")
        print("5. Salir del sistema")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            registrar_expediente()
        elif opcion == "2":
            listar_expedientes()
        elif opcion == "3":
            buscar_expediente()
        elif opcion == "4":
            ordenar_por_folios_burbuja()
        elif opcion == "5":
            print("\nGracias por utilizar la Mesa de Partes Digital. ¡Hasta luego!")
        else:
            print("\n[ERROR]: Opción no válida. Intente nuevamente.")

# Arrancar la aplicación
if __name__ == "__main__":
    menu_principal()


