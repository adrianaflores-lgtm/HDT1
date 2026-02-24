# ============================================================
#  HDT1 — Parte 1: Condicionales
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 1.1 — Precios Dinámicos de Entradas  (10 pts)
# ============================================================
# Precios base: campo=Q200, gradería=Q350, preferencia=Q600, vip=Q1200
#
# Descuento mayor aplica (NO acumulables entre sí):
#   - Estudiante UFM con carnet válido    → 25%
#   - Compra en los primeros 30 días  → 15%
#   - Menor de 12 O mayor de 64 años      → 50%
#
# Regla adicional (sí aplica SOBRE el precio ya descontado):
#   - Más de 4 entradas de la misma zona  → 10% extra



# --- Datos de prueba (NO modificar) ---
zona          = "vip"
edad          = 30
es_ufm        = True
carnet_valido = True
dias_anticipacion = 35
cantidad      = 5

# --- Tu código aquí ---

# TODO 1: Determina el precio base según zona
if zona == "campo":
    precio_base = 200
elif zona == "gradería":
    precio_base = 350
elif zona == "preferencia":
    precio_base = 600
elif zona == "vip":
    precio_base = 1200
else:
    precio_base = 0

# TODO 2: Calcula el porcentaje de descuento más alto que aplica
descuento = 0
motivo = "ninguno"
if edad < 12 or edad > 64:
    descuento = 0.50
    motivo = "edad"
elif es_ufm and carnet_valido:
    descuento = 0.25
    motivo = "estudiante UFM"
elif dias_anticipacion <= 30:
    descuento = 0.15
    motivo = "compra anticipada"


# TODO 3: Aplica el descuento al precio base
precio_por_entrada = precio_base * (1 - descuento)

# TODO 4: Si cantidad > 4, aplica 10% adicional sobre el precio descontado
descuento_volumen = 0
if cantidad > 4:
    descuento_volumen = (precio_por_entrada * cantidad) * 0.10

total = (precio_por_entrada * cantidad) - descuento_volumen

# TODO 5: Imprime el resumen con el formato esperado:

print("=== ENTRADA DATAFEST 2026 ===")
print(f"Zona:{zona}")
print(f"Precio base: Q{precio_base:.2f}")
print(f"Descuento: {descuento*100}% ({motivo})")
print(f"Precio/entrada: Q{precio_por_entrada:.2f}")
print(f"Descuento volumen ({cantidad} entradas): -Q{descuento_volumen:.2f}")
print(f"TOTAL A PAGAR: Q{total:.2f}")


# ============================================================
#  Ejercicio 1.2 — Control de Acceso al Festival  (10 pts)
# ============================================================
# Evalúa TODAS las reglas en orden:
#   1. Sin entrada válida             → denegado
#   2. Zona vip/backstage sin pulsera → denegado
#   3. Menor de 18 sin acompañante    → denegado
#   4. prohibicion = True             → denegado (siempre)
#   5. Si pasa todo lo anterior       → permitido
#
# Formato: "Caso N: [PERMITIDO/DENEGADO] mensaje"

# --- Datos de prueba (NO modificar) ---
casos_acceso = [
    # (zona,         edad, tiene_entrada, pulsera_especial, con_acompanante, prohibicion)
    ("vip",          25,   False,         True,             True,            False),  # sin entrada
    ("vip",          22,   True,          False,            True,            False),  # sin pulsera
    ("campo",        16,   True,          False,            False,           False),  # menor sin acomp.
    ("preferencia",  30,   True,          False,            True,            False),  # todos ok
]

# --- Tu código aquí ---

for i, caso in enumerate(casos_acceso, start=1):
    zona_c, edad_c, entrada, pulsera, acompanante, prohibicion = caso

    if not entrada:
        estado = "denegado"
        mensaje = "Sin entrada valida"
    elif (zona_c == "vip" or zona_c == "backstage") and not pulsera:
        estado = "denegado"
        mensaje = "zona vip requiere pulsera especial"
    elif edad_c < 18 and not acompanante:
        estado = "denegado"
        mensaje = "menor de edad requiere acompañante"
    elif prohibicion: 
        estado = "denegado"
        mensake = "Acceso restringido por seguridad"
    else:
        estado = "permitido"
        mensaje = f"Bienvenido/a a zona: {zona_c}"
    print(f"Caso {i}: [{estado}] {mensaje}")

# Salida esperada:
# Caso 1: [DENEGADO] Sin entrada válida
# Caso 2: [DENEGADO] Zona VIP requiere pulsera especial
# Caso 3: [DENEGADO] Menor de edad requiere acompañante
# Caso 4: [PERMITIDO] Bienvenido/a a zona: preferencia
