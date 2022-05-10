# Este programa corresponde a una calculadora simple
# Desarrollador: Luis Miguel Guerrero

# Esta funcion agrega dos numeros
def add(x, y):
    return x + y

# Esta funcion resta dos numeros
def subtract(x, y):
    return x - y

# Esta funcion multiplica dos numeros
def multiply(x, y):
    return x * y

# Esta funcion divide dos numeros
def divide(x, y):
    return x / y


print("Selecciona la operación que deseas usar.")
print("1.Suma")
print("2.Resta")
print("3.Multiplicar")
print("4.Dividir")

while True:
    # Imput para el usuario
    choice = input("Ingresa (1/2/3/4): ")

    # Tome una opcion para el inicio del calculo
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Agregue el primer numero: "))
        num2 = float(input("Agregue el segundo numero: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            if num2==0:
                print("error")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Necesita otro calculo? (si/no): ")
        if next_calculation == "no":
          break
            
    
    else:
        print("Invalid Input")