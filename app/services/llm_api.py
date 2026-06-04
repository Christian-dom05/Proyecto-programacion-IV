import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def generar_codigo_simulacion(prompt_usuario, api_key):
    """
    Se conecta a la API de IA, envía el pedido del usuario y retorna ÚNICAMENTE
    el código en Python para la simulación 3D.
    """
    
    # 1. La URL de destino (Usamos Gemini 2.5 Flash por su altísima velocidad)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    # 2. El "System Prompt" (Ingeniería de Prompts para máxima optimización)
    # Aquí le quitamos toda la "personalidad" a la IA para que solo devuelva código puro.
    instrucciones_sistema = """
    Eres un motor de renderizado que solo escupe código Python.
    Tu objetivo es crear simulaciones visuales en 3D basándote en la petición del usuario.
    
    REGLAS ESTRICTAS E INQUEBRANTABLES:
    1. Usa SIEMPRE matplotlib.pyplot y mpl_toolkits.mplot3d.
    2. Responde ÚNICAMENTE con código Python válido.
    3. CERO formato Markdown. NO uses etiquetas como ```python o ```.
    4. CERO saludos, CERO explicaciones. Solo el código.
    5. Asegúrate de incluir plt.show() al final para que la ventana se abra.
    6. PROHIBIDO importar librerías del sistema como os, sys, subprocess, eval o exec.
    """

    # 3. El Paquete (Payload) estructurado en formato JSON
    payload = {
        "system_instruction": {
            "parts": [{"text": instrucciones_sistema}]
        },
        "contents": [
            {"parts": [{"text": prompt_usuario}]}
        ],
        "generationConfig": {
            "temperature": 0.1 # Temperatura baja para que sea preciso y no alucine
        }
    }

    # Cabeceras de la petición
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # 4. El Envío de la petición a internet
        respuesta = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Si Google nos rechaza, imprimimos su excusa exacta
        if respuesta.status_code != 200:
            return f"\n--- GOOGLE NOS RECHAZÓ ---\nCódigo: {respuesta.status_code}\nDetalle: {respuesta.text}"
            
        respuesta.raise_for_status() 
        
        # 5. Extraer solo el texto del JSON de respuesta
        datos = respuesta.json()
        codigo_generado = datos['candidates'][0]['content']['parts'][0]['text']
        
        # Limpieza extra por si la IA es terca y pone las comillas de Markdown
        codigo_limpio = codigo_generado.replace("```python", "").replace("```", "").strip()
        
        return codigo_limpio

    except Exception as e:
        return f"# Error de conexión local: {e}"
# ==========================================
# ZONA DE PRUEBAS
# ==========================================
if __name__ == "__main__":
    # OJO: Para probar esto, se necesita de una API KEY gratuita de Google Studio AI.
    # Reemplazar 'TU_API_KEY_AQUI' con la clave real.
    MI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    if not MI_API_KEY:
        print("no se encontró la API KEY en el .env")
    else:
        print("Enviando petición a la IA... (midiendo velocidad)")
        
        # Simulamos que le hablaste al micrófono
        mi_pedido = "Simula una superficie 3D de un paraboloide hiperbólico, usa colores llamativos."
        
        codigo_recibido = generar_codigo_simulacion(mi_pedido, MI_API_KEY)
        
        print("\n--- CÓDIGO RECIBIDO DE LA IA ---")
        print(codigo_recibido)
        print("--------------------------------")
        print("\n¡Éxito! Como ves, no hay texto de relleno, está listo para ser ejecutado.")