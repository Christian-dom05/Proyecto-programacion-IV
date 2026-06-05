import pyttsx3
import speech_recognition as sr

def inicializar_motor_voz():
    engine = pyttsx3.init()
    # Buscar una voz en español instalada en tu Windows
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'spanish' in voice.name.lower() or 'es' in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break
    # Ajustar la velocidad de habla para que suene natural
    engine.setProperty('rate', 160)
    return engine

motor = inicializar_motor_voz()

def hablar(texto):
    """Convierte texto a voz y lo reproduce por los altavoces."""
    print(f"🤖 Jarvis dice: {texto}")
    motor.say(texto)
    motor.runAndWait()

def escuchar():
    """Captura el audio del micrófono y usa IA de Google para pasarlo a texto."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Jarvis está ajustando el ruido de fondo... (silencio un segundo)")
        r.adjust_for_ambient_noise(source, duration=1)
        
        hablar("Te escucho, señor.")
        print("🟢 ¡Habla ahora!")
        
        try:
            # Escucha hasta que dejas de hablar
            audio = r.listen(source, timeout=5, phrase_time_limit=15)
            print("⏳ Procesando el audio...")
            
            # Convierte el audio a texto
            texto = r.recognize_google(audio, language="es-ES")
            print(f"👤 Escuchado: '{texto}'")
            return texto
            
        except sr.UnknownValueError:
            hablar("No pude entender lo que dijiste.")
            return None
        except sr.RequestError:
            hablar("Error de conexión con el satélite de voz.")
            return None
        except Exception:
            return None