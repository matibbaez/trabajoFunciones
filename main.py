import math

# Define las funciones que has creado

# Función para calcular el área de un círculo.
def area_circulo(radio):
    return math.pi * radio ** 2

# Función para verificar si un número es par o impar.
def calcular_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Función para calcular la suma de una lista de números.
suma = []

def suma_numeros(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Función para encontrar el máximo de tres números.
numeros_ingresados = []

def encontrar_maximo(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Función para invertir una cadena.
def invertir_cadena(cadena):
    lista = list(cadena)
    lista.reverse()
    cadena_invertida = "".join(lista)
    return cadena_invertida

# Función para ordenar alfabéticamente una lista de palabras.
def ordenar_palabras(lista_palabras):
    lista_palabras = []

    while True:
        palabra_ingresada = input("Ingrese una palabra: ")
        if palabra_ingresada.isalpha():
            lista_palabras.append(palabra_ingresada)
            print("Palabra ingresada con éxito")
        else:
            print("Palabra no válida")
        
        continuar = input("Desea continuar? s/n ")
        if continuar.lower() != "s":
            break

    lista_palabras.sort()

    lista_formateada = ", ".join(lista_palabras)

    print(f"Lista de palabras ordenadas alfabéticamente: {lista_formateada}")

# Función para calcular la potencia de un número.
def calcular_potencia(base, exponente):
    return base ** exponente

# Función para obtener una lista de números pares.
lista_numeros = []

def solo_pares(lista_numeros):
    numeros_pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares

# Funcion que determine si una cadena dada es un palíndromo
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

# Función que tome una lista de números y calcule el producto de todos los elementos.
numeros = []

def calcular_producto(lista):
    producto = 1 
    
    for numero in lista:
        producto *= numero
    
    return producto

# Menú de opciones
while True:
    print("\nMenú de opciones:")
    print("1. Calcular el área de un círculo")
    print("2. Verificar si un número es par o impar")
    print("3. Calcular la suma de una lista de números")
    print("4. Encontrar el máximo de tres números")
    print("5. Invertir una cadena")
    print("6. Ordenar alfabéticamente una lista de palabras")
    print("7. Calcular la potencia de un número")
    print("8. Obtener una lista de números pares")
    print("9. Calcular el producto de todos los elementos.")
    print("10. Determinar si una cadena dada es un palíndromo.")

    opcion = input("Elija una opción (1-10): ")

    if opcion == '1':
        radio = float(input("Ingrese el radio del círculo: "))
        print(f"El área del círculo es: {area_circulo(radio)}")
    elif opcion == '2':
        numero = int(input("Ingrese un número: "))
        print(f"El número es {calcular_par_impar(numero)}.")
    elif opcion == '3':
        while True:
            numero = input("Ingrese un número (o 'fin' para terminar): ")
            if numero == 'fin':
                break
            try:
                numero = float(numero)
                suma.append(numero)
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")
        print(f"La suma de los números ingresados es: {suma_numeros(suma)}")
    elif opcion == '4':
        for i in range(3):
            numero_ingresado = input("Ingrese un número:")
            try:
                numero_ingresado = int(numero_ingresado)
                if numero_ingresado > 0:
                    numeros_ingresados.append(numero_ingresado)
                else:
                    print("El número debe ser mayor que 0.")
            except:
                print("No es un número válido")
        print(encontrar_maximo(*numeros_ingresados))
    elif opcion == '5':
        cadena_original = input("Ingrese una cadena: ")
        cadena_invertida = invertir_cadena(cadena_original)
        print(cadena_invertida)
    elif opcion == '6':
        ordenar_palabras()
    elif opcion == '7':
        base = float(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        print(f"{base} elevado a la {exponente} es igual a {calcular_potencia(base, exponente)}")
    elif opcion == '8':
        while True:
            numero = input("Ingrese su número (o 'fin' para terminar): ")
            
            if numero == 'fin':
                break
            
            try:
                numero = int(numero) 
                lista_numeros.append(numero)     
            except:
                print("Entrada inválida. Ingrese un número válido.")
        numeros_pares = solo_pares(lista_numeros)
        print(f"Números pares en la lista: {numeros_pares}")
    elif opcion == '9':
        while True:
            numero = input("Ingrese su número (o 'fin' para terminar): ")
            
            if numero == 'fin':
                break
            
            try:
                numero = int(numero) 
                numeros.append(numero)     
            except:
                print("Entrada inválida. Ingrese un número válido.")
        resultado = calcular_producto(numeros)
        print(f"El producto de los números en la lista es: {resultado}")
    elif opcion == '10':
        cadena = input("Ingrese una palabra o frase: ")
        resultado = es_palindromo(cadena)
        if resultado:
            print("La palabra o frase ingresada es un palíndromo.")
        else:
            print("La palabra o frase ingresada no es un palíndromo.")
    else:
        print("Opción no válida. Elija una opción del 1 al 10.")