# ============================================================
#  HDT1 — Parte 2: Strings
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 2.1 — Generador de Credenciales  (8 pts)
# ============================================================
# Formato: FD26-[ZONA3]-[INICIALES][NUMERO]
#
#   ZONA3     → primeras 3 letras de la zona en MAYÚSCULAS
#   INICIALES → primera letra del nombre + primera del apellido, MAYÚSCULAS
#   NUMERO    → registro con 4 dígitos y ceros a la izquierda
#
# Pistas:
#   - nombre.split()     → lista de palabras; el apellido es el ÚLTIMO elemento
#   - str(n).zfill(4)    → "47" → "0047"
#   - "campo"[:3].upper() → "CAM"
#
# Casos de prueba (NO modificar):
registros = [
    ("Carlos Mendoza",        "vip",         47),
    ("Ana García",            "campo",         5),
    ("José Luis Rodríguez",   "gradería",   1823),
    ("María López",           "preferencia", 312),
]

# --- Tu código aquí ---

for nombre, zona, numero in registros:
    zona3 = zona[:3].upper()

    partes = nombre.split()
    inicial_nombre = partes[0][0].upper()
    inicial_apellido = partes[-1][0].upper()

    num4 = str(numero).zfill(4)

    credencial = f"FD26-{zona3}-{inicial_nombre}{inicial_apellido}{num4}"
    print(credencial)

# Salida esperada:
# FD26-VIP-CM0047
# FD26-CAM-AG0005
# FD26-GRA-JR1823
# FD26-PRE-ML0312


# ============================================================
#  Ejercicio 2.2 — Limpieza de Datos de Asistentes  (6 pts)
# ============================================================
# Formato crudo: "  nombre  ,  email  ,  edad  "
#
# Procesamiento:
#   - Separar por coma y limpiar espacios con .strip()
#   - Nombre: .title() para capitalizar cada palabra
#   - Email:  .lower(); válido si contiene "@" y hay un "." DESPUÉS del "@"
#   - Edad:   int(); advertir si no está en [5, 100]

# --- Datos de prueba (NO modificar) ---
registros_crudos = [
    "  ana GARCIA    ,   ana.garcia@gmail.com  ,   22  ",
    "  JOSE LUIS perez  ,  jl_perez@outlook  ,  17  ",
    "  María Fernanda SOLIS  ,  mfernanda@ufm.edu  ,  150  ",
]

# --- Tu código aquí ---

for i, registro in enumerate(registros_crudos, start=1):
    print(f"--- Registro {i} ---")

    partes = registro.split(",")
    nombre_crudo = partes[0].strip()
    email_crudo = partes[1].strip()
    edad_cruda  = partes[2].strip()

    nombre_limpio = nombre_crudo.title()

    email_limpio = email_crudo.lower()
    tiene_arroba = "@" in email_limpio
    valido_email = False
    if tiene_arroba:
        pos_arroba = email_limpio.find("@")
        # debe haber un "." después del "@"
        if "." in email_limpio[pos_arroba+1:]:
            valido_email = True
    
    edad = int(edad_cruda)
    en_rango = (edad >= 5 and edad <= 100)

    print(f"Nombre : {nombre_limpio}")
    print(f"Email  : {email_limpio} | Válido: {'Sí' if valido_email else 'No'}")

    if en_rango:
        print(f"Edad   : {edad} | En rango: Sí")
    else:
        print(f"Edad   : {edad} | En rango: No — fuera del rango [5, 100]")

    print()



# Salida esperada:
# --- Registro 1 ---
# Nombre : Ana Garcia
# Email  : ana.garcia@gmail.com | Válido: Sí
# Edad   : 22 | En rango: Sí
#
# --- Registro 2 ---
# Nombre : Jose Luis Perez
# Email  : jl_perez@outlook | Válido: No
# Edad   : 17 | En rango: Sí
#
# --- Registro 3 ---
# Nombre : Maria Fernanda Solis
# Email  : mfernanda@ufm.edu | Válido: Sí
# Edad   : 150 | En rango: No — fuera del rango [5, 100]


# ============================================================
#  Ejercicio 2.3 — Análisis de Reseñas  (6 pts)
# ============================================================
# Para cada reseña calcula:
#   1. Total de palabras (.split())
#   2. Total de vocales (a e i o u á é í ó ú — mayúsculas y minúsculas)
#   3. Palabra más larga (primer empate gana)
#   4. Sentimiento:
#      - positiva   → solo tiene palabras positivas
#      - negativa   → solo tiene palabras negativas
#      - mixta      → tiene de ambas
#      - neutral    → no tiene ninguna
#
# Positivas: "increíble", "excelente", "genial", "espectacular",
#            "maravilloso", "fantástico"
# Negativas: "malo", "pésimo", "terrible", "aburrido",
#            "decepcionante", "horrible"

# --- Datos de prueba (NO modificar) ---
resenas = [
    "El festival fue espectacular los artistas son increíble el sonido la energía todo genial",
    "Lamentablemente el sonido fue terrible aunque los artistas estuvieron genial pero el acceso horrible",
]

# --- Tu código aquí ---

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
palabras_positivas = ["increíble", "excelente", "genial", "espectacular", "maravilloso", "fantástico"]
palabras_negativas = ["malo", "pésimo", "terrible", "aburrido", "decepcionante", "horrible"]

signos = ".,;:¡!¿?\"()"

for i, resena in enumerate(resenas, start=1):
    print(f"--- Reseña {i} ---")

    # 1) contar palabras
    palabras = resena.split()
    total_palabras = len(palabras)

    # 2) contar vocales
    total_vocales = 0
    for ch in resena:
        if ch in vocales:
            total_vocales += 1

    # 3) palabra más larga (primer empate gana)
    palabra_larga = ""
    for p in palabras:
        p_limpia = p.strip(signos)
        if len(p_limpia) > len(palabra_larga):
            palabra_larga = p_limpia

    # 4) sentimiento
    tiene_pos = False
    tiene_neg = False

    for p in palabras:
        w = p.strip(signos).lower()
        if w in palabras_positivas:
            tiene_pos = True
        if w in palabras_negativas:
            tiene_neg = True

    if tiene_pos and not tiene_neg:
        sentimiento = "positiva"
    elif tiene_neg and not tiene_pos:
        sentimiento = "negativa"
    elif tiene_pos and tiene_neg:
        sentimiento = "mixta"
    else:
        sentimiento = "neutral"

    print(f"Palabras      : {total_palabras}")
    print(f"Vocales       : {total_vocales}")
    print(f"Palabra larga : \"{palabra_larga}\"")
    print(f"Sentimiento   : {sentimiento}")
    print()

# Salida esperada:
# --- Reseña 1 ---
# Palabras      : 14
# Vocales       : 27
# Palabra larga : "espectacular"
# Sentimiento   : positiva
#
# --- Reseña 2 ---
# Palabras      : 12
# Vocales       : 22
# Palabra larga : "decepcionante"
# Sentimiento   : mixta
