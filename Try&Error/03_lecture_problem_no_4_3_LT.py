from datetime import datetime

try:
    # Leidžiame vartotojui įvesti norimą datą ir laiką
    data_string = input("Įveskite datą ir laiką formatu 'YYYY-MM-DD HH:MM:SS': ")
    ivesta_data = datetime.strptime(data_string, '%Y-%m-%d %H:%M:%S')

    # Gauname dabartinę datą ir laiką
    dabar = datetime.now()

    # Paskaičiuojame, kiek laiko praėjo nuo įvestos datos
    praėjęs_laikas = dabar - ivesta_data

    # Paskaičiuojame ir atspausdiname metus, mėnesius, dienas, valandas, minutes ir sekundes
    metai = praėjęs_laikas.days // 365
    print("Metų: ", round(metai))

    menesiai = (praėjęs_laikas.days % 365) // 30
    print("Mėnesių: ", round(menesiai))

    dienos = praėjęs_laikas.days % 30
    print("Dienų: ", dienos)

    valandos = praėjęs_laikas.seconds // 3600
    print("Valandų: ", valandos)

    minutes = (praėjęs_laikas.seconds % 3600) // 60
    print("Minučių: ", minutes)

    sekundes = praėjęs_laikas.seconds % 60
    print("Sekundžių: ", sekundes)
except ValueError:
    print("Klaida: neteisingas datos ir laiko formatas. Turėtų būti 'YYYY-MM-DD HH:MM:SS'.")
