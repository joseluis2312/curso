def decorador_log(func):
 def wrapper(*args, **kwargs):
 print(f"Llamando a {func.__name__} con argumentos {args} y
{kwargs}")
 resultado = func(*args, **kwargs)
 print(f"{func.__name__} retornó {resultado}")
 return resultado
 return wrapper
class CalculadoraDecorada:
 @decorador_log
 def suma(self, a, b):
 return a + b
# Usamos la clase
calc = CalculadoraDecorada()
print("Resultado de la suma:", calc.suma(5, 3)) # Resultado: Llamando
a suma...