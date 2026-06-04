# main.py

import os
from dotenv import load_dotenv

# Importamos nuestros propios módulos
from app.services.llm_api import generar_codigo_simulacion
from app.executors.runner import ejecutar_simulacion

def iniciar_jarvis():
    print("="*50)
    print("🤖 JARVIS: Módulo Generador de Simulaciones")
    print("="*50)
    
    # Cargamos la API Key desde tu archivo .env de forma segura
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") 
    
    if not api_key:
        print("Error: No se encontró la variable GEMINI_API_KEY en el archivo .env")
        return

    # Por ahora la entrada es por teclado, en la siguiente fase activaremos el micrófono
    comando_usuario = input("\nUsuario: ")
    
    print("\n🤖 Jarvis: Procesando cálculos lógicos y espaciales...")
    codigo_generado = generar_codigo_simulacion(comando_usuario, api_key)
    
    if codigo_generado.startswith("# Error"):
        print(f"\n🤖 Jarvis: Imposible contactar al servidor base. {codigo_generado}")
        return

    # Pasamos el código al motor para su renderizado final
    ejecutar_simulacion(codigo_generado)

if __name__ == "__main__":
    iniciar_jarvis()