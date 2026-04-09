import json
import os

ARCHIVO_DATOS = "datos.json"

class Vehiculo:
    
    def __init__(self, id_vehiculo, marca, modelo, año, precio_dia, disponible=True):
        self.id_vehiculo = id_vehiculo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_dia = float(precio_dia)
        self.disponible = disponible
    
    def to_dict(self):
        
        return {
            'id_vehiculo': self.id_vehiculo,
            'marca': self.marca,
            'modelo': self.modelo,
            'año': self.año,
            'precio_dia': self.precio_dia,
            'disponible': self.disponible
        }
    
    @staticmethod
    def from_dict(datos):
        
        return Vehiculo(
            datos['id_vehiculo'],
            datos['marca'],
            datos['modelo'],
            datos['año'],
            datos['precio_dia'],
            datos['disponible']
        )
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Alquilado"
        return f"ID: {self.id_vehiculo} | {self.marca} {self.modelo} ({self.año}) | ${self.precio_dia}/día | {estado}"

def cargar_vehiculos():
    
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    
    try:
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return [Vehiculo.from_dict(v) for v in datos]
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def guardar_vehiculos(vehiculos):
    
    with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as archivo:
        json.dump([v.to_dict() for v in vehiculos], archivo, indent=2, ensure_ascii=False)

def registrar_vehiculo(vehiculos):

    from utils import mostrar_titulo, pausar, imprimir_mensaje
    
    mostrar_titulo("REGISTRAR NUEVO VEHÍCULO")
    
    try:
        id_vehiculo = input("ID del vehículo: ").strip()
        
        if any(v.id_vehiculo == id_vehiculo for v in vehiculos):
            imprimir_mensaje("Ya existe un vehículo con ese ID", "error")
            pausar()
            return
        
        marca = input("Marca: ").strip()
        modelo = input("Modelo: ").strip()
        año = int(input("Año: "))
        precio_dia = float(input("Precio por día: $"))
        
        nuevo_vehiculo = Vehiculo(id_vehiculo, marca, modelo, año, precio_dia)
        vehiculos.append(nuevo_vehiculo)
        guardar_vehiculos(vehiculos)
        
        imprimir_mensaje(f"¡Vehículo {marca} {modelo} registrado exitosamente!", "exito")
    except ValueError:
        imprimir_mensaje("Error: Año y precio deben ser números válidos", "error")
    except Exception as e:
        imprimir_mensaje(f"Error: {str(e)}", "error")
    
    pausar()

def consultar_vehiculos(vehiculos):
    
    from utils import mostrar_titulo, pausar, imprimir_mensaje
    
    mostrar_titulo("CONSULTAR VEHÍCULOS")
    
    if not vehiculos:
        imprimir_mensaje("No hay vehículos registrados.", "error")
        pausar()
        return
    
    print(f"Total de vehículos: {len(vehiculos)}\n")
    
    for vehiculo in vehiculos:
        print(str(vehiculo))
        print("-" * 60)
    
    print("\nOpciones:")
    print("1. Buscar por ID")
    print("2. Buscar por marca")
    print("3. Ver solo disponibles")
    print("4. Volver al menú principal")
    
    opcion = input("\nSeleccione una opción: ").strip()
    
    if opcion == "1":
        buscar_por_id(vehiculos)
    elif opcion == "2":
        buscar_por_marca(vehiculos)
    elif opcion == "3":
        mostrar_disponibles(vehiculos)
    
    pausar()

def buscar_por_id(vehiculos):
    
    from utils import imprimir_mensaje
    
    id_buscar = input("\nIngrese el ID del vehículo: ").strip()
    vehiculo = next((v for v in vehiculos if v.id_vehiculo == id_buscar), None)
    
    if vehiculo:
        print("\n" + "=" * 60)
        imprimir_mensaje("VEHÍCULO ENCONTRADO:", "exito")
        print(str(vehiculo))
        print("=" * 60)
    else:
        imprimir_mensaje("Vehículo no encontrado", "error")

def buscar_por_marca(vehiculos):
    
    from utils import imprimir_mensaje
    
    marca_buscar = input("\nIngrese la marca: ").strip().lower()
    encontrados = [v for v in vehiculos if marca_buscar in v.marca.lower()]
    
    if encontrados:
        print(f"\nVehículos de marca {marca_buscar.upper()}:")
        print("-" * 60)
        for v in encontrados:
            print(str(v))
    else:
        imprimir_mensaje(f"No se encontraron vehículos de marca {marca_buscar}", "error")

def mostrar_disponibles(vehiculos):
    
    from utils import imprimir_mensaje
    
    disponibles = [v for v in vehiculos if v.disponible]
    
    if disponibles:
        print("\nVEHÍCULOS DISPONIBLES:")
        print("-" * 60)
        for v in disponibles:
            print(str(v))
    else:
        imprimir_mensaje("No hay vehículos disponibles en este momento", "error")

def editar_vehiculo(vehiculos):
    from utils import mostrar_titulo, pausar, imprimir_mensaje
    
    mostrar_titulo("EDITAR VEHÍCULO")
    
    if not vehiculos:
        imprimir_mensaje("No hay vehículos para editar.", "error")
        pausar()
        return
    
    id_editar = input("Ingrese el ID del vehículo a editar: ").strip()
    vehiculo = next((v for v in vehiculos if v.id_vehiculo == id_editar), None)
    
    if not vehiculo:
        imprimir_mensaje("Vehículo no encontrado", "error")
        pausar()
        return
    
    print("\nDatos actuales:")
    print(str(vehiculo))
    print("\nDeje en blanco para mantener el valor actual")
    
    try:
        nueva_marca = input(f"Nueva marca ({vehiculo.marca}): ").strip()
        if nueva_marca:
            vehiculo.marca = nueva_marca
        
        nuevo_modelo = input(f"Nuevo modelo ({vehiculo.modelo}): ").strip()
        if nuevo_modelo:
            vehiculo.modelo = nuevo_modelo
        
        nuevo_año = input(f"Nuevo año ({vehiculo.año}): ").strip()
        if nuevo_año:
            vehiculo.año = int(nuevo_año)
        
        nuevo_precio = input(f"Nuevo precio por día ({vehiculo.precio_dia}): ").strip()
        if nuevo_precio:
            vehiculo.precio_dia = float(nuevo_precio)
        
        cambiar_dispo = input("¿Cambiar disponibilidad? (s/n): ").strip().lower()
        if cambiar_dispo == 's':
            vehiculo.disponible = not vehiculo.disponible
            estado = "disponible" if vehiculo.disponible else "alquilado"
            imprimir_mensaje(f"Estado cambiado a {estado}", "info")
        
        guardar_vehiculos(vehiculos)
        imprimir_mensaje("Vehículo actualizado exitosamente", "exito")
        
    except ValueError:
        imprimir_mensaje("Error: Año y precio deben ser números válidos", "error")
    
    pausar()

def eliminar_vehiculo(vehiculos):
    """Elimina un vehículo del sistema"""
    from utils import mostrar_titulo, pausar, imprimir_mensaje
    
    mostrar_titulo("ELIMINAR VEHÍCULO")
    
    if not vehiculos:
        imprimir_mensaje("No hay vehículos para eliminar.", "error")
        pausar()
        return
    
    id_eliminar = input("Ingrese el ID del vehículo a eliminar: ").strip()
    vehiculo = next((v for v in vehiculos if v.id_vehiculo == id_eliminar), None)
    
    if not vehiculo:
        imprimir_mensaje("Vehículo no encontrado", "error")
        pausar()
        return
    
    print("\nVehículo a eliminar:")
    print(str(vehiculo))
    
    confirmar = input("\n¿Está seguro de eliminar este vehículo? (s/n): ").strip().lower()
    
    if confirmar == 's':
        vehiculos.remove(vehiculo)
        guardar_vehiculos(vehiculos)
        imprimir_mensaje("Vehículo eliminado exitosamente", "exito")
    else:
        imprimir_mensaje("Operación cancelada", "info")
    
    pausar()