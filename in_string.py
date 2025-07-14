def check_vowels():
    # Ingresar el nombre
    nombre = input("Ingrese un nombre: ")
    # Convertir a minúsculas para evitar errores con mayúsculas
    nombre = nombre.lower()

# Verificar presencia de cada vocal (sin tildes)
print("Contiene a:", "a" in nombre)
print("Contiene e:", "e" in nombre)
print("Contiene i:", "i" in nombre)
print("Contiene o:", "o" in nombre)
print("Contiene u:", "u" in nombre)
