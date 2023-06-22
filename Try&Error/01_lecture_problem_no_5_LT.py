sk1 = float(input("Įveskite pirmą skaičių: "))
sk2 = float(input("Įveskite antrą skaičių: "))

veiksmas = input("Pasirinkite matematinį veiksmą (+, -, *, /): ")

if veiksmas == "+":
    rezultatas = sk1 + sk2
    print("Suma:", rezultatas)
elif veiksmas == "-":
    rezultatas = sk1 - sk2
    print("Skirtumas:", rezultatas)
elif veiksmas == "*":
    rezultatas = sk1 * sk2
    print("Daugyba:", rezultatas)
elif veiksmas == "/":
    if sk2 != 0:
        rezultatas = sk1 / sk2
        print("Dalyba:", rezultatas)
    else:
        print("Klaida: dalyba iš nulio negalima!")
else:
    print("Klaida: neatpažintas matematinis veiksmas!")

