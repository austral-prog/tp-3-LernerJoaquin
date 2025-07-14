def slice_advanced():
    texto = input("Escriba su oración: ")

    if len(texto) < 5:
        print("El texto debe tener al menos 5 caracteres.")
    else:
        resultado = texto[4::2]
        print("Resultado:", resultado)
