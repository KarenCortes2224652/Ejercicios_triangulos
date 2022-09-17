# Dados tres números a, b y c, verificar si se pueden formar lados de un triángulo.

print("-----------------------------------")
print("--- LADOS - DE - UN - TRIANGULO ---")
print("-----------------------------------")

#Input
A=int(input("Digite el primer lado:"))
B=int(input("Digite el segundo lado:"))
C=int(input("Digite el tercer lado:"))

#Processing

if (A+B)>C and (A+C)>B and (B+C)>A:
    print("\n Si se forma un triangulo")
else:
    print("\n No se forma un triangulo")

#Finish