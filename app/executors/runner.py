# app/executors/runner.py

import traceback
from app.core.security import es_codigo_seguro

def ejecutar_simulacion(codigo_python):
    """
    Verifica la seguridad del código y, si es seguro, lo compila y lo ejecuta 
    en tiempo real para levantar la interfaz visual.
    """
    es_seguro, mensaje = es_codigo_seguro(codigo_python)
    
    if not es_seguro:
        print(f"\n[!] ALERTA DE SEGURIDAD: {mensaje}")
        return False
        
    print("\n[+] Protocolo de seguridad aprobado. Renderizando entorno 3D...")
    
    try:
        # La función nativa 'exec' corre el string como si fuera código Python real.
        # Le pasamos globals() para que tenga acceso al entorno de ejecución principal.
        exec(codigo_python, globals())
        return True
    except Exception as e:
        print(f"\n[-] Error crítico durante la simulación física/matemática: {e}")
        # traceback nos ayuda a ver exactamente en qué línea falló el código de la IA
        traceback.print_exc()
        return False