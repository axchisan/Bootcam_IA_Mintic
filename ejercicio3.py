nota1 = float(input("ingrese la nota 1: "))
nota2 = float(input("ingrese la nota 2: "))
nota3 = float(input("ingrese la nota 3: "))

nota1 *= 0.30
nota2 *= 0.50
nota3 *= 0.20

promedio = nota1+nota2+nota3
print(f"el promedio del estudiante es: {promedio:.1f}")

