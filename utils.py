import os
import platform

def limpiar_pantalla():
    
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def mostrar_titulo(titulo):
    
    limpiar_pantalla()
    print("=" * 60)
    print(f"  {titulo}")
    print("=" * 60)
    print()

def pausar():
    input("\nPresione Enter para continuar...")

def imprimir_mensaje(texto, tipo="info"):
    
    if tipo == "error":
        print(f" {texto}")
    elif tipo == "exito":
        print(f" {texto}")
    elif tipo == "info":
        print(f"  {texto}")
    else:
        print(texto)
