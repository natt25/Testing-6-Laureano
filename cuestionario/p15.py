def raiz_cuadrada(x):
    assert x >= 0, "No se puede calcular la raiz cuadrada de un numero negativo"
    return x ** 0.5

print(raiz_cuadrada(25))  # Salida: 5.0
print(raiz_cuadrada(-4))  # Lanza una excepcion
