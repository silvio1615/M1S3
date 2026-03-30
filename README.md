# M1S3
# 📦 Sistema de Inventario PRO

Sistema de gestión de inventario por consola desarrollado en Python. Permite agregar, buscar, actualizar y eliminar productos, calcular estadísticas y persistir datos en archivos CSV.

---

## 🗂️ Estructura del proyecto

```
inventario/
├── app.py          # Módulo principal, ejecuta el menú e interactúa con el usuario
├── servicio.py     # Lógica de negocio (agregar, buscar, eliminar, estadísticas)
├── archivos.py     # Manejo de archivos CSV (guardar y cargar)
└── inventario.csv  # Archivo generado al guardar el inventario
```

---

## ⚙️ Requisitos

- Python 3.8 o superior
- No requiere librerías externas

---

## 🚀 Cómo ejecutar

```bash
python app.py
```

---

## 📋 Menú de opciones

| Opción | Descripción |
|--------|-------------|
| 1 | Agregar producto |
| 2 | Mostrar inventario |
| 3 | Buscar producto |
| 4 | Ver estadísticas |
| 5 | Guardar inventario en CSV |
| 6 | Cargar inventario desde CSV |
| 7 | Actualizar producto |
| 8 | Eliminar producto |
| 9 | Salir |

---

## 📌 Funcionalidades

- **Agregar**: Registra un producto con nombre, precio y cantidad. No permite duplicados.
- **Mostrar**: Lista todos los productos en formato tabla.
- **Buscar**: Encuentra un producto por nombre sin distinguir mayúsculas.
- **Estadísticas**: Calcula unidades totales, valor total del inventario, producto más caro y el de mayor stock.
- **Guardar CSV**: Exporta el inventario actual a `inventario.csv`.
- **Cargar CSV**: Importa productos desde `inventario.csv` con opción de sobrescribir o fusionar.
- **Actualizar**: Modifica el precio y/o cantidad de un producto existente.
- **Eliminar**: Elimina un producto con confirmación previa.

---

## 🔄 Diagrama de flujo

```mermaid
flowchart TD
    A([Inicio]) --> B[Mostrar menú]
    B --> C{Opción}

    C -->|1| D[Agregar producto]
    D --> D1{¿Ya existe?}
    D1 -->|Sí| D2[Avisar duplicado] --> B
    D1 -->|No| D3[Agregar a lista] --> B

    C -->|2| E[Mostrar inventario] --> B

    C -->|3| F[Buscar producto]
    F --> F1{¿Encontrado?}
    F1 -->|Sí| F2[Mostrar datos] --> B
    F1 -->|No| F3[Avisar no encontrado] --> B

    C -->|4| G[Calcular estadísticas]
    G --> G1{¿Inventario vacío?}
    G1 -->|Sí| G2[Avisar sin datos] --> B
    G1 -->|No| G3[Mostrar métricas] --> B

    C -->|5| H[Guardar CSV] --> B

    C -->|6| I[Cargar CSV]
    I --> I1{¿Sobrescribir o fusionar?}
    I1 -->|Sobrescribir| I2[Reemplazar lista] --> B
    I1 -->|Fusionar| I3[Combinar listas] --> B

    C -->|7| J[Actualizar producto]
    J --> J1{¿Existe?}
    J1 -->|Sí| J2[Modificar precio/cantidad] --> B
    J1 -->|No| J3[Avisar no encontrado] --> B

    C -->|8| K[Eliminar producto]
    K --> K1{¿Confirmar?}
    K1 -->|Sí| K2{¿Existe?}
    K2 -->|Sí| K3[Eliminar de lista] --> B
    K2 -->|No| K4[Avisar no encontrado] --> B
    K1 -->|No| K5[Cancelar] --> B

    C -->|9| L([Salir])
```

---

## 💾 Formato del CSV

El archivo `inventario.csv` generado tiene la siguiente estructura:

```
nombre,precio,cantidad
Manzana,1.5,10
Pera,2.0,5
```

---

## 🧠 Decisiones de diseño

- El inventario vive en memoria (`inventario_memoria`) mientras el programa corre.
- La lógica de negocio está separada del módulo principal en `servicio.py` para facilitar su reutilización.
- El manejo de archivos está aislado en `archivos.py` para mantener responsabilidades separadas.
- Las búsquedas son insensibles a mayúsculas y minúsculas.
- La carga de CSV valida cada fila individualmente y cuenta las filas omitidas por errores.

--
