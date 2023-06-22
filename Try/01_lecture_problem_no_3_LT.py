zodziai = []

n = int(input("Įveskite žodžių kiekį: "))

for i in range(n):
    zodis = input("Įveskite žodį: ")
    zodziai.append(zodis)

print("Įvesti žodžiai:")
for i, zodis in enumerate(zodziai, start=1):
    print(f"Žodis {i}: {zodis}, ilgis: {len(zodis)}")

