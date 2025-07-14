def slice_simple():
    texto = input("Ingrese un texto: ").lower()

    # Primeras 3 letras
    primeras_3 = texto[0:3]

    # Las 3 letras del medio
    longitud = len(texto)
    medio = longitud // 2
    if longitud >= 3:
        tres_del_medio = texto[medio - 1 : medio + 2]
    else:
        tres_del_medio = texto  # en caso de texto muy corto

    # De la primera a la cuarta letra (incluida)
    primeras_4 = texto[0:4]

    # De la antepenúltima a la última letra (usando índices positivos)
    antepenultima_a_ultima = texto[len(texto)-3:]

    # Mostrar resultados
    print("Primeras 3 letras:", primeras_3)
    print("3 letras del medio:", tres_del_medio)
    print("De la primera a la cuarta:", primeras_4)
    print("De la antepenúltima a la última:", antepenultima_a_ultima)
