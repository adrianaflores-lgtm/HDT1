# ============================================================
#  HDT1 — Parte 5: Integrador
#  DataFest 2026 — Sistema de Taquilla Virtual
# ============================================================
#
# Construye un sistema de taquilla interactivo usando while.
# Combina todo lo aprendido: ciclos, condicionales, strings y listas.
#
# ⚠ No uses diccionarios ni funciones con def.
# ⚠ Para calcular el total de mis_compras usa un for (no sum()).

# ============================================================
#  Datos del festival (NO modificar)
# ============================================================

cartel = [
    ("Resonancia",     "Rock",        "Apertura"),
    ("Voz del Sur",    "Folk",        "Apertura"),
    ("La Guardia",     "Reggaeton",   "Soporte"),
    ("Eco Urbano",     "Hip-Hop",     "Soporte"),
    ("Marimba 2.0",    "Folk",        "Soporte"),
    ("Pixel Dreams",   "Electrónica", "Principal"),
    ("Bass Station",   "Electrónica", "Principal"),
    ("Los Caminos",    "Rock",        "Principal"),
    ("Tierra Roja",    "Rock",        "Headliner"),
    ("Circuito",       "Electrónica", "Headliner"),
]

# Precios base por zona (simplificados, sin descuentos)
zonas_validas  = ["campo", "gradería", "preferencia", "vip"]
precios_base   = [200,     350,        600,           1200 ]
# Uso: precios_base[zonas_validas.index("vip")] → 1200

# Lista donde se guardarán las compras: cada elemento es [zona, cantidad, total]
mis_compras = []

# ============================================================
#  Sistema de taquilla
# ============================================================

print("=" * 40)
print("     TAQUILLA DATAFEST 2026")
print("=" * 40)

opcion = ""

while opcion != "5":
    print("\n1. Ver cartel de artistas")
    print("2. Comprar entrada")
    print("3. Ver mis compras")
    print("4. Resumen de gastos")
    print("5. Salir")
    opcion = input("\nElige una opción: ")

    # ----------------------------------------------------------
    if opcion == "1":
    # ----------------------------------------------------------
        print("\n=== CARTEL DATAFEST 2026 ===")
        for i, (nombre, genero, turno) in enumerate(cartel, start=1):
            print(f"[{i}] {nombre} ({genero}) — Turno: {turno}")

    # ----------------------------------------------------------
    elif opcion == "2":
    # ----------------------------------------------------------
        zona = input("Ingresa la zona (campo/gradería/preferencia/vip): ").strip().lower()

        while zona not in zonas_validas:
            print("Zona no válida")
            zona = input("Ingresa la zona (campo/gradería/preferencia/vip): ").strip().lower()

        cantidad = int(input("Ingresa la cantidad de entradas: "))

        idx = zonas_validas.index(zona)
        precio = precios_base[idx]
        total = precio * cantidad

        mis_compras.append([zona, cantidad, total])

        print("\n✓ Compra realizada:")
        print(f"  Zona      : {zona}")
        print(f"  Cantidad  : {cantidad} entradas")
        print(f"  Total     : Q{total:.2f}")

    # ----------------------------------------------------------
    elif opcion == "3":
    # ----------------------------------------------------------
        if len(mis_compras) == 0:
            print("Aún no has comprado entradas.")
        else:
            print("\n=== MIS COMPRAS ===")
            for i, compra in enumerate(mis_compras, start=1):
                zona_c = compra[0]
                cantidad_c = compra[1]
                total_c = compra[2]
                print(f"Compra {i} | Zona: {zona_c} | Cantidad: {cantidad_c} | Total: Q{total_c:.2f}")

    # ----------------------------------------------------------
    elif opcion == "4":
    # ----------------------------------------------------------
        if len(mis_compras) == 0:
            print("Aún no has realizado ninguna compra.")
        else:
            print("\n=== RESUMEN DE GASTOS ===")

            # total gastado (sin sum)
            total_gastado = 0
            for compra in mis_compras:
                total_gastado += compra[2]

            # total entradas
            total_entradas = 0
            for compra in mis_compras:
                total_entradas += compra[1]

            # zona favorita (sin diccionarios)
            zonas_contadas = []
            conteos = []

            for compra in mis_compras:
                z = compra[0]
                if z in zonas_contadas:
                    pos = zonas_contadas.index(z)
                    conteos[pos] += 1
                else:
                    zonas_contadas.append(z)
                    conteos.append(1)

            # encontrar la zona con mayor conteo (con for)
            zona_favorita = zonas_contadas[0]
            max_conteo = conteos[0]

            for i in range(len(conteos)):
                if conteos[i] > max_conteo:
                    max_conteo = conteos[i]
                    zona_favorita = zonas_contadas[i]

            print(f"Total gastado    : Q{total_gastado:.2f}")
            print(f"Total entradas   : {total_entradas}")
            print(f"Zona favorita    : {zona_favorita}")

    # ----------------------------------------------------------
    elif opcion == "5":
    # ----------------------------------------------------------
        print("\n¡Gracias por usar la taquilla de DataFest 2026!")
        print("Nos vemos en el festival. 🎵")

    # ----------------------------------------------------------
    else:
    # ----------------------------------------------------------
        print("Opción no válida. Intenta de nuevo.")