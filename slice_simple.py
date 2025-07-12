texto = input("Ingresá una palabra: ")
texto = texto.lower()
primeras_3 = texto[0:3]
mitad = len(texto) // 2
inicio_medio = mitad - 1
letras_medio = texto[inicio_medio:inicio_medio + 3]
prim_a_cuarta = texto[0:4]
ultimas_3 = texto[-3:]
print(primeras_3)
print(letras_medio)
print(prim_a_cuarta + ultimas_3)    
