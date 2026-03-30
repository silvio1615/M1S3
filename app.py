import servicio
import archivos

# Lista principal que almacena los productos en memoria mientras el programa corre
inventario_memoria = []
running = True

while running:
    servicio.menu()
    opcion = input("Seleccione: ")

    if opcion == "1":
        try:
            nom = input("Nombre: ")
            pre = float(input("Precio: "))
            can = int(input("Cantidad: "))
            # No se permiten valores negativos
            if pre < 0 or can < 0:
                print("Solo números positivos.")
                continue
            servicio.agregar_producto(inventario_memoria, nom, pre, can)
        except ValueError:
            print(" Error: Precio/Cantidad deben ser números.")

    elif opcion == "2":
        servicio.mostrar_inventario(inventario_memoria)

    elif opcion == "3":
        nom = input("Nombre del producto a buscar: ")
        p = servicio.buscar_producto(inventario_memoria, nom)
        # Si encontró el producto lo muestra, si no avisa
        if p:
            print(f" Encontrado: {p['nombre']} | ${p['precio']} | Stock: {p['cantidad']}")
        else:
            print(" Producto no encontrado.")

    elif opcion == "4":
        stats = servicio.calcular_estadisticas(inventario_memoria)
        if stats:
            print(f"\n--- ESTADÍSTICAS ---")
            print(f"║  Unidades totales: {stats['unidades']:>8} ║")
            print(f"Valor Total: ${stats['valor_total']:.2f}")
            print(f"Producto más caro: {stats['mas_caro']['nombre']} ({stats['mas_caro']['precio']})")
            print(f"║  Mayor stock      : {stats['mayor_stock']['nombre'][:7]:>7} ║")
        else:
            print("Sin datos.")

    elif opcion == "5":
        archivos.guardar_csv(inventario_memoria, "inventario.csv")

    elif opcion == "6":
        nuevos, err = archivos.cargar_csv("inventario.csv")
        if nuevos:
            modo = input("¿Sobrescribir inventario actual (S) o Fusionar (F)? Sobrescribir es irreversible: ").upper()
            if modo == "S":
                # Borra todo el inventario actual y lo reemplaza con el del CSV
                inventario_memoria.clear()
                inventario_memoria.extend(nuevos)
            else:
                # Fusiona: si el producto ya existe suma cantidad y actualiza precio
                for n in nuevos:
                    existente = servicio.buscar_producto(inventario_memoria, n["nombre"])
                    if existente:
                        existente["cantidad"] += n["cantidad"]
                        existente["precio"] = n["precio"]
                    else:
                        inventario_memoria.append(n)
            print(f" Carga lista. Filas omitidas: {err}")

    elif opcion == "7":
        nom = input("Nombre del producto a actualizar: ")
        p = servicio.buscar_producto(inventario_memoria, nom)
        if p:
            print("Deje en blanco para no cambiar el valor.")
            try:
                n_pre = input(f"Nuevo precio (actual: {p['precio']}): ")
                n_can = input(f"Nueva cantidad (actual: {p['cantidad']}): ")
                # Solo convierte si el usuario escribió algo
                pre = float(n_pre) if n_pre else None
                can = int(n_can) if n_can else None
                servicio.actualizar_producto(inventario_memoria, nom, pre, can)
                print("Producto actualizado.")
            except ValueError:
                print(" Error: Precio/Cantidad deben ser números.")
        else:
            print(" No se encontró el producto.")

    elif opcion == "8":
        nom = input("Nombre del producto a eliminar: ")
        # Pide confirmación antes de eliminar ya que es irreversible
        confirmar = input(f"¿Seguro que deseas eliminar '{nom}'? (S/N): ").upper()
        if confirmar == "S":
            eliminado = servicio.eliminar_producto(inventario_memoria, nom)
            if eliminado:
                print(f" Se ha eliminado: {eliminado['nombre']}")
            else:
                print(" No se pudo eliminar (no existe).")
        else:
            print(" Eliminación cancelada.")

    elif opcion == "9":
        # Cambia running a False para salir del bucle
        running = False
