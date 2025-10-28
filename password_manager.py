from argon2 import PasswordHasher
from getpass import getpass

def main():
    ph = PasswordHasher(
        time_cost=3,
        memory_cost=64 * 1024,
        parallelism=4
    )

    pwd = getpass("Ingresa la contraseña: ")
    hashed = ph.hash(pwd)
    print("\nHash (lista para guardar en DB):")
    print(hashed)

    intento = getpass("\nVerifica la contraseña (vuelve a ingresarla): ")
    try:
        if ph.verify(hashed, intento):
            print("La se verificó correctamente.")
    except Exception as e:
        print("La verificación ha fracasado", str(e))

if __name__ == "__main__":
    main()
