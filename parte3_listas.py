# ============================================================
#  HDT1 — Parte 3: Listas
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 3.1 — Gestión de Zona VIP  (10 pts)
# ============================================================
# Sigue el orden exacto de operaciones indicado.
# ⚠ No hagas todas las operaciones de una sola vez —
#   el estado intermedio de las listas importa para la calificación.

# --- Datos de prueba (NO modificar) ---
lista_espera = ["Valentina", "Diego", "Alejandra", "Kim", "Lu", "Marcelo", "Nati"]
capacidad_vip = 5
zona_vip = []

# --- Tu código aquí ---

# Operación 1: Agregar "Óscar" y "Paula" al FINAL de lista_espera
lista_espera.append("Óscar")
lista_espera.append("Paula")

# Operación 2: "Diego" cancela — removerlo de lista_espera
lista_espera.remove("Diego")

# Operación 3: Mover las primeras `capacidad_vip` personas a zona_vip
contador = 0
while contador < capacidad_vip:
    persona = lista_espera.pop(0)
    zona_vip.append(persona)
    contador += 1

# Operación 4: Añadir " ★" a nombres con MÁS DE 5 caracteres
for i in range(len(zona_vip)):
    if len(zona_vip[i]) > 5:
        zona_vip[i] = zona_vip[i] + " ★"

# Operación 5: Imprimir estado final
print(f"ZONA VIP ({len(zona_vip)}/{capacidad_vip})  : {zona_vip}")
print(f"EN ESPERA ({len(lista_espera)})   : {lista_espera}")

# Salida esperada:
# ZONA VIP (5/5)  : ['Valentina ★', 'Alejandra ★', 'Kim', 'Lu', 'Marcelo ★']
# EN ESPERA (3)   : ['Nati', 'Óscar', 'Paula']


# ============================================================
#  Ejercicio 3.2 — Ajuste de Precios con IVA  (10 pts)
# ============================================================
# IVA Guatemala = 12%  →  precio_sin_iva = precio_con_iva / 1.12

# --- Datos de prueba (NO modificar) ---
precios_con_iva = [224.00, 392.00, 672.00, 1344.00, 56.00, 448.00]

# --- Tu código aquí ---

# a) Lista con todos los precios sin IVA
precios_sin_iva = []

for precio in precios_con_iva:
    sin_iva = round(precio / 1.12, 2)
    precios_sin_iva.append(sin_iva)

# b) Solo los precios sin IVA menores a Q400
precios_accesibles = []

for precio in precios_sin_iva:
    if precio < 400:
        precios_accesibles.append(precio)

# c) Lista formateada
precios_formateados = []

for precio in precios_sin_iva:
    precios_formateados.append(f"Q{precio:.2f}")

print(f"Sin IVA        : {precios_sin_iva}")
print(f"Accesibles     : {precios_accesibles}")
print(f"Formateados    : {precios_formateados}")

# Salida esperada:
# Sin IVA        : [200.0, 350.0, 600.0, 1200.0, 50.0, 400.0]
# Accesibles     : [200.0, 350.0, 50.0]
# Formateados    : ['Q200.00', 'Q350.00', 'Q600.00', 'Q1200.00', 'Q50.00', 'Q400.00']
