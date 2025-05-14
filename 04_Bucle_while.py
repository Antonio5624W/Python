adivina = 0
intentos = 0

while adivina != 6 and intentos < 5:
    adivina = int(input("Adivina el numero: "))
    intentos = intentos + 1
     
if adivina != 6:
    print("Te quedaste sin intentos:(")
else:
    print("Lo entendistee!")