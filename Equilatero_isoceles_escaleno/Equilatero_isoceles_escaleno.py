# Determinar si un triángulo es equilátero, isóceles o escaleno.

print("----------------------------------------")
print("--- EQUILÁTERO - ISÓCELES - ESCALENO ---")
print("----------------------------------------")

#Input
A=int(input("Digite el primer lado:"))
B=int(input("Digite el segundo lado:"))
C=int(input("Digite el tercer lado:"))

#Processing
if ( A + B ) > C and ( A + C ) > B and ( B + C ) > A :
    print("\n Si es un triángulo" )
if (A == B == C):
    print ("Es un triángulo equilátero")
elif (A == B or A == C or B == C):
    print ("Es un triángulo isóceles")
else :
    print ("Es un triángulo escaleno")

#Fin