from vehiculo import cargar_vehiculos, registrar_vehiculo, consultar_vehiculos, editar_vehiculo, eliminar_vehiculo
from utils import limpiar_pantalla, mostrar_titulo, pausar, imprimir_mensaje

def mostrar_menu():
    print("\n" + "=" * 60)
    print("  SISTEMA DE ALQUILER DE VEHÍCULOS ")
    print("=" * 60)
    print("-" * 60)
    print("  1.  Registrar nuevo vehículo")
    print("  2.  Consultar vehículos")
    print("  3.   Editar vehículo")
    print("  4.   Eliminar vehículo")
    print("  5.  Ver estadísticas")
    print("  6.  Salir")
    print("-" * 60)

def mostrar_estadisticas(vehiculos):
    mostrar_titulo("ESTADÍSTICAS DEL SISTEMA")
    
    total = len(vehiculos)
    disponibles = sum(1 for v in vehiculos if v.disponible)
    alquilados = total - disponibles
    
    if total > 0:
        precio_promedio = sum(v.precio_dia for v in vehiculos) / total
        print(f" Total de vehículos: {total}")
        print(f" Vehículos disponibles: {disponibles}")
        print(f" Vehículos alquilados: {alquilados}")
        print(f" Precio promedio por día: ${precio_promedio:.2f}")
        
        mas_caro = max(vehiculos, key=lambda v: v.precio_dia)
        mas_barato = min(vehiculos, key=lambda v: v.precio_dia)
        
        print(f"\n Vehículo más caro: {mas_caro.marca} {mas_caro.modelo} (${mas_caro.precio_dia}/día)")
        print(f" Vehículo más económico: {mas_barato.marca} {mas_barato.modelo} (${mas_barato.precio_dia}/día)")
        
        años = [v.año for v in vehiculos]
        print(f"\n Año más reciente: {max(años)}")
        print(f" Año más antiguo: {min(años)}")
        
        from collections import Counter
        marcas = [v.marca for v in vehiculos]
        marca_comun = Counter(marcas).most_common(1)[0]
        print(f" Marca más común: {marca_comun[0]} ({marca_comun[1]} vehículos)")
        
    else:
        imprimir_mensaje("No hay vehículos registrados en el sistema", "error")
    
    print("\n" + "=" * 60)
    pausar()

def main():
    vehiculos = cargar_vehiculos()
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        opcion = input("\n  Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            registrar_vehiculo(vehiculos)
        elif opcion == "2":
            consultar_vehiculos(vehiculos)
        elif opcion == "3":
            editar_vehiculo(vehiculos)
        elif opcion == "4":
            eliminar_vehiculo(vehiculos)
        elif opcion == "5":
            mostrar_estadisticas(vehiculos)
        elif opcion == "6":
            limpiar_pantalla()
            print("\n" + "=" * 60)
            imprimir_mensaje("¡Gracias por usar el Sistema de Alquiler de Vehículos!", "exito")
            imprimir_mensaje("¡Hasta luego! ", "exito")
            print("=" * 60 + "\n")
            break
        else:
            imprimir_mensaje("Opción inválida. Por favor, seleccione 1-6", "error")
            pausar()

if __name__ == "__main__":
    main()