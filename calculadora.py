def calculadora(operacion:str, *parametros:tuple[int, ...]) -> int:
    resultado = 0
    if operacion == "SUMA":
        for numero in parametros:
            resultado += numero
    
    elif operacion == "RESTA":
        resultado = parametros[0]
        if len(parametros) == 1:
            print(parametros)
            pass
        else:
            for numero in parametros[1:]:
                resultado -= numero

    else:
        raise "Operacion incorrecta"
    
    return resultado

print(calculadora("RESTA", 10))