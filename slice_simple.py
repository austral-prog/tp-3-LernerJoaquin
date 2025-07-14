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
        tres_del_medio = texto 

    primeras_4 = texto[0:4]

    antepenultima_a_ultima = texto[len(texto)-3:]

    print("Primeras 3 letras:", primeras_3)
    print("3 letras del medio:", tres_del_medio)
    print("De la primera a la cuarta:", primeras_4)
    print("De la antepenúltima a la última:", antepenultima_a_ultima)
