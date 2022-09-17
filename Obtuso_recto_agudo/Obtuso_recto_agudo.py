# Determinar si un triángulo es obtuso, recto o agudo.

print("-----------------------------------")
print("--- OBTUSO - RECTO - AGUDO ---")
print("-----------------------------------")
  
#Input
A=int(input("Digite el ángulo A: "))
B=int(input("Digite el ángulo B: "))
C=int(input("Digite el ángulo C: "))

#Processing
if A + B + C== 180:
      print("\n Si es un triángulo")
else:
    print("\n No es un triángulo")
if A+B<90  or C + B <90 or A + C <90:
    print("\nEl triángulo es obtuso")
elif A+B == 90 or B+C == 90 or C+A ==90:
    print("\nEl triángulo es recto")
elif A+B>90 or B+C>90 or C+B>90:
    print("\nEl triángulo es agudo")

#Fin