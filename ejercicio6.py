def calcular_suma(lista_numeros):
    suma = 0  
    for numero in lista_numeros:
        suma += numero  
    return suma

entrada = input("Ingresa una lista de números separados por comas: ")

lista_numeros = [int(x) for x in entrada.split(',')]

resultado = calcular_suma(lista_numeros)
print("La suma de los números es:", resultado)
