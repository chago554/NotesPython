def mostrar_menu():
    print("""
    -------------Calculadora-------------
    Selecciona la operación:
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    """)

def obtener_numeros():
    while True:
        try:
            numero1 = int(input("Ingrese el primer número: "))
            numero2 = int(input("Ingrese el segundo número: "))
            return numero1, numero2
        except ValueError:
            print("Por favor, ingrese números válidos.")


def suma(numero1, numero2):
    return numero1 + numero2
    
def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2
     
def division(numero1, numero2):
    return numero1 / numero2


mostrar_menu()

while True:
    opcion = input("Ingrese la opción (1-4): ")
    if opcion in "1234":
        num1, num2 = obtener_numeros()
        if opcion == "4" and num2 == 0:
            print("No se puede dividir entre cero.")
        else:
            if opcion == "1":
                resultado = suma(num1, num2)
            elif opcion == "2":
                resultado = resta(num1, num2)
            elif opcion == "3":
                resultado = multiplicacion(num1, num2)
            elif opcion == "4":
                resultado = division(num1, num2)  
            print(f"Resultado = {resultado}")
        break 
    else:
        print("Opción inválida. Intente nuevamente.")


