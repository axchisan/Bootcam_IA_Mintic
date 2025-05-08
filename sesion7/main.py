print("BIenvenidos al entrenamiento con python, vamos a disfrutar al aximo esta sesion")

""""
    Descuento en una compra:
    si compras más de $10000, obtienes un descuento del 20%
    pide el monto de la  compra y muestra el precio final

"""

#pedir datos por teclado al usuario int entero float decimales stc cadenas de caracteres bool booleanos

compra = float(input("DIgite el valor de la compra: "))
#di compras mas de $1000, obtienes un descuento del 20%
#siempre que la salida tenga más de un camino de resolució, debo implementar condicionales
#operadores combinados 
#operadores de asignacion =, operadores aritméticos +-*/, operadores lógicos and y, or o, not,
#operadores de comparacion ==, !=, >, <, >=, <=

if compra > 1000:
    descuento = compra * 0.2
    #compra = compra - descuento #operador de asignacion
    compra -= descuento #operador de asignación compuesto
    print(f"El descento es de {descuento}, por lo tanto su valor  a pagar es: {compra}")