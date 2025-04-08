def dividir(a, b):
    assert b != 0, "Divisor no puede ser cero"  # Precondicion
    resultado = a / b
    assert resultado >= 0, "Resultado debe ser positivo o cero"  # Postcondicion
    return resultado

print(dividir(10, 2))  # Salida: 5.0
print(dividir(10, 0))  # Lanza un error debido a la precondicion
