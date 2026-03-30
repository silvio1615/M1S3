import csv

def guardar_csv(inventario, ruta):
    """
    Guarda el inventario en un archivo CSV.
    
    Args:
        inventario: lista de productos a guardar
        ruta: ruta del archivo CSV destino
    """
    if not inventario:
        print(" No hay nada que guardar.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
            # Escribe la fila de encabezados
            writer.writeheader()
            # Escribe todos los productos
            writer.writerows(inventario)
        print(f"Inventario guardado en: {ruta}")
    except Exception as e:
        print(f" Error al guardar: {e}")

def cargar_csv(ruta):
    """
    Lee y valida los productos desde un archivo CSV.
    
    Args:
        ruta: ruta del archivo CSV a leer
    
    Returns:
        Tupla con la lista de productos válidos y el número de filas omitidas.
    """
    productos_cargados = []
    errores = 0  # Contador de filas inválidas
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                try:
                    # Valida y convierte cada campo de la fila
                    nombre = fila["nombre"].strip()
                    if not nombre: raise ValueError
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    # No se permiten valores negativos
                    if precio < 0 or cantidad < 0: raise ValueError
                    
                    productos_cargados.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except (ValueError, KeyError):
                    errores += 1
        return productos_cargados, errores
    except FileNotFoundError:
        print(" Archivo no encontrado.")
        return [], 0
