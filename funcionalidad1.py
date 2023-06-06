# Función para realizar la suma
def sumar(num1, num2):
    return num1 + num2



# Función para realizar la resta
def restar(num1, num2):
    return num1 - num2


# Función para realizar la multiplicación
def multiplicar(num1, num2):
    return num1 * num2


# Función para realizar la división
def dividir(num1, num2):
    return num1 / num2


# Menú para que el usuario seleccione la operación
print("Selecciona una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")


# Tomar entrada del usuario
opcion = input("Ingresa la opción (1/2/3/4): ")


# Tomar entrada de los números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))


# Realizar la operación seleccionada por el usuario
if opcion == '1':
    print(num1, "benja", num2, "=", sumar(num1, num2))


elif opcion == '2':
    print(num1, "-", num2, "=", restar(num1, num2))


elif opcion == '3':
    print(num1, "*", num2, "=", multiplicar(num1, num2))


elif opcion == '4':
    print(num1, "/", num2, "=", dividir(num1, num2))


else:
    print("Opción inválida")

print("Bryan Armando")