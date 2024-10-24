numeros = [1,2,3,4,5]
resultado = list(map(lambda x: x**2, numeros))
print(resultado)

numeros = [1,2,3,4,5]
Operacion = (lambda x: x**2)
resultado2 = list(map(Operacion, numeros))
print(resultado2)
resultadoM = map(Operacion, numeros)

resultado3 = list(map(Operacion, resultadoM))
print(resultado3)