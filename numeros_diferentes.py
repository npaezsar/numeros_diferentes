"""Programa 7:
Verificar si dos numeros son diferentes"""

print("-----------------------")
print("--Numeros diferentes?--")
print("-----------------------")

# input
x = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y: "))

# processing
if x != y:
    msj = "Son diferentes"
else:
    msj = "Son iguales"

# output
print("Los numeros " + msj)