def sumar (num1, num2):
    return num1 + num2

def restar (num1, num2):
    return num1 - num2

def cal_sumar(parametros:tuple[int, ...]) -> int:
    resultado = 0
    for i in range(1, len(parametros)):
        resultado+= parametros[i]
    return resultado

def cal_restar(parametros:tuple[int, ...]) -> int:
    resultado = 0
    for i in range(1, len(parametros)):
        resultado-= parametros[i]
    return resultado

# Realizar una funcion sumatriai o resta en la cual reciba n parametros
# Sumar | Restar
# List | Tuple | Dict | Set ...todas son ordenadas
def calculadora(operacion:str, *parametros:tuple[int, ...]) -> int:
    if operacion == "suma":
        return cal_sumar(*parametros)
    elif operacion == "resta":
        return cal_restar(*parametros)
    else:
        raise ValueError("Operacion no valida")



    #pass
    # if operacion == "suma":
    #     return sum(*parametros)
    # elif operacion == "resta":
    #     return restar(*parametros)
    # else:
    #     raise ValueError("Operacion no valida")
    # pass