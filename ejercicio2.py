"""pide dos numeros decimales al usuario
    realiza operaciones basicas como suma, resta, multiplicacion
    y division
    muestra los resultados en pantalla, con la división mostrando solo dos decimales
"""

num1 = float(input("Ingresa el primer numero : "))
num2 = float(input("Ingresa el sergundo numero : "))

#operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

#prints de operaciones 
print(f"el resultado de la suma es: {suma}")
print(f"el resultado de la resta es: {resta}")
print(f"el resultado de la multiplicacion es: {multiplicacion}")
print(f"el resultado de la division es: {division:.2f}")
