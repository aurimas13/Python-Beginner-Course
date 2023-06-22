suma = 0

while True:
    skaicius = float(input("Įveskite skaičių: "))
    
    if skaicius > 0:
        suma += skaicius
        continue
    else:
        break

print("Teigiamų skaičių suma:", suma)

