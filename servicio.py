def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto nuevo al inventario.
    
    Args:
        inventario: lista donde se almacenan los productos
        nombre: nombre del producto
        precio: precio unitario del producto
        cantidad: unidades disponibles
    
    Returns:
        True si se agregó correctamente, False si ya existía.
    """
    producto = {
        "nombre": nombre, 
        "precio": precio, 
        "cantidad": cantidad
        }
    # Verifica que no exista un producto con el mismo nombre
    if buscar_producto(inventario, nombre) is not None:
        print(f"  [!] Ya existe un producto llamado '{nombre}'.")
        return False
    
    inventario.append(producto)
    print(f" {nombre} agregado correctamente.")
    return True

def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario en formato tabla.
    
    Args:
        inventario: lista donde se almacenan los productos
    """
    if not inventario:
        print("Empty inventory.")
        return
    print("\n--- INVENTARIO ACTUAL ---")
    # Recorre cada producto y lo imprime con formato
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Stock: {producto['cantidad']}")

def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre en el inventario.
    
    Args:
        inventario: lista donde se almacenan los productos
        nombre: nombre del producto a buscar
    
    Returns:
        El diccionario del producto si existe, None si no se encontró.
    """
    # Compara ignorando mayúsculas y minúsculas
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def calcular_estadisticas(inventario):
    """
    Calcula métricas clave del inventario.
    
    Args:
        inventario: lista donde se almacenan los productos
    
    Returns:
        Diccionario con unidades totales, valor total, producto más caro
        y producto con mayor stock. None si el inventario está vacío.
    """
    if not inventario: return None

    # Lambda para calcular el subtotal de un producto
    subtotal = lambda p: p["precio"] * p["cantidad"]
    
    # Suma total de unidades y valor monetario
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    
    # Busca el producto más caro y el de mayor stock
    mas_caro = max(inventario, key=lambda x: x["precio"])
    mayor_stock = max(inventario, key=lambda x: x["cantidad"])

    return {
        "unidades": unidades_totales,
        "valor_total": valor_total,
        "mas_caro": mas_caro,
        "mayor_stock": mayor_stock
    }    

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o cantidad de un producto existente.
    
    Args:
        inventario: lista donde se almacenan los productos
        nombre: nombre del producto a actualizar
        nuevo_precio: nuevo precio a asignar, None para no cambiar
        nueva_cantidad: nueva cantidad a asignar, None para no cambiar
    
    Returns:
        True si se actualizó correctamente, False si no se encontró.
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        # Solo actualiza los campos que el usuario proporcionó
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por su nombre.
    
    Args:
        inventario: lista donde se almacenan los productos
        nombre: nombre del producto a eliminar
    
    Returns:
        El diccionario del producto eliminado, None si no existía.
    """
    for i, p in enumerate(inventario):
        # Compara ignorando mayúsculas y minúsculas
        if p["nombre"].lower() == nombre.lower():
            return inventario.pop(i)
    return None

def menu():
    """Muestra el menú principal de opciones del sistema."""
    print("\n=== SISTEMA DE INVENTARIO PRO ===")
    print("1. Agregar | 2. Mostrar | 3. Buscar | 4. Estadísticas")
    print("5. Guardar CSV | 6. Cargar CSV | 7. Actualizar | 8. Eliminar | 9. Salir")
