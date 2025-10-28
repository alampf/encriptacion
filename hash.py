import hashlib
import getpass


def hashear_contrasena():
    """
    Solicita una contraseña por consola (ocultando la entrada)
    y muestra su hash SHA-256.
    """
    print("--- Generador de Hash SHA-256 ---")

    # Usamos getpass para que la contraseña no se muestre al escribir
    # Esto es una buena práctica de seguridad
    try:
        contrasena = getpass.getpass("Introduce la contraseña a hashear: ")
    except Exception as e:
        print(f"Error al leer la contraseña: {e}")
        return

    # 1. Codificar la cadena de texto (string) a bytes
    # Los algoritmos de hash como SHA-256 operan sobre bytes, no sobre cadenas de texto.
    contrasena_bytes = contrasena.encode("utf-8")

    # 2. Crear el objeto hash
    # Se recomienda usar SHA-256 o superior para nuevas implementaciones.
    hash_objeto = hashlib.sha256(contrasena_bytes)

    # 3. Obtener el hash final en formato hexadecimal
    hash_hex = hash_objeto.hexdigest()

    print("\n--- Resultado ---")
    print(f"Contraseña introducida (no visible): {'*' * len(contrasena)}")
    print(f"Algoritmo utilizado: SHA-256")
    print(f"*Hash generado (Hexadecimal):*\n{hash_hex}")


if __name__ == "__main__":
    hashear_contrasena()
