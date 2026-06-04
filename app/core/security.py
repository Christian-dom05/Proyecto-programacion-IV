
def es_codigo_seguro(codigo):
    """
    Analiza el código generado para evitar la ejecución de comandos maliciosos
    a nivel de sistema operativo.
    """
    # Módulos y funciones críticas que la IA no tiene por qué usar para hacer gráficas 3D
    palabras_prohibidas = [
        'os.', 'sys.', 'subprocess', 'socket', 
        'eval(', 'exec(', 'open(', '__import__'
    ]
    
    for palabra in palabras_prohibidas:
        if palabra in codigo:
            return False, f"Vulnerabilidad detectada: Intento de uso del módulo reservado '{palabra}'"
            
    # Validamos que el código efectivamente tenga la intención de graficar
    if 'matplotlib' not in codigo:
        return False, "El código generado no parece contener instrucciones gráficas de Matplotlib."

    return True, "Código limpio."