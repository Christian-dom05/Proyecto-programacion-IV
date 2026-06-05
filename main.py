# main.py

import os
from dotenv import load_dotenv

# Importamos nuestros módulos (ahora incluimos el de voz)
from app.services.llm_api import generar_codigo_simulacion
from app.executors.runner import ejecutar_simulacion
from app.services.voice import hablar, escuchar

def iniciar_jarvis():
    print("="*50)
    print("🤖 Jarvis: En línea")
    print("="*50)
    
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") 
    
    if not api_key:
        print("Error: No se encontró la variable GEMINI_API_KEY en el .env")
        return

    hablar("Sistemas en línea. Protocolos de simulación activados.")

    # Bucle infinito: Jarvis se queda esperando órdenes
    while True:
        comando_usuario = escuchar()
        
        if comando_usuario is None:
            continue # Si no entendió, vuelve a escuchar
            
        # Palabra clave para apagar el sistema
        if "apagar" in comando_usuario.lower() or "salir" in comando_usuario.lower():
            hablar("Apagando sistemas. Hasta la próxima.")
            break

        hablar("Procesando cálculos espaciales.")
        print("\n🤖 Jarvis: Redactando código con IA...")
        
        codigo_generado = generar_codigo_simulacion(comando_usuario, api_key)
        
        if codigo_generado.startswith("# Error"):
            hablar("Señor, no pude conectar con el servidor principal.")
            continue

        hablar("Renderizando entorno tridimensional en pantalla.")
        
        # Ejecuta la simulación
        ejecutar_simulacion(codigo_generado)
        
        # Una vez que cierras la ventana de Matplotlib, vuelve a escuchar
        hablar("Simulación finalizada.")

if __name__ == "__main__":
    iniciar_jarvis()