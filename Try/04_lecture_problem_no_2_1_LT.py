import datetime

# Funkcija, patikrinanti asmens kodo validumą
def ar_validus_asmens_kodas(kodas):
    """Patikrina, ar paduotas asmens kodas yra validus."""
    # Asmens kodas turi būti 11 skaitmenų ilgio
    if len(kodas) != 11:
        return False
    # Pirmas skaitmuo nurodo lytį ir gimimo šimtmetį
    lytis_gimimo_simtmetyje = int(kodas[0])
    if lytis_gimimo_simtmetyje < 1 or lytis_gimimo_simtmetyje > 6:
        return False
    # Sekančios šešios skaitmenys nurodo gimimo datą
    try:
        datetime.datetime.strptime(kodas[1:7], "%y%m%d")
    except ValueError:
        return False
    # Likusios skaitmenys yra unikalus numeris, kuris turi būti didesnis už 0
    if int(kodas[7:]) <= 0:
        return False
    return True

# Funkcija, generuojanti asmens kodą
def generuoti_asmens_koda(lytis, gimimo_data, eiles_nr):
    """Generuoja asmens kodą pagal įvestą lytį, gimimo datą ir eilės numerį."""
    # Pirmas skaitmuo nurodo lytį ir gimimo šimtmetį
    if gimimo_data.year < 1900:
        pirmas_skaitmuo = 1 if lytis == "vyras" else 2
    elif gimimo_data.year < 2000:
        pirmas_skaitmuo = 3 if lytis == "vyras" else 4
    else:
        pirmas_skaitmuo = 5 if lytis == "vyras" else 6
    # Sekančios šešios skaitmenys nurodo gimimo datą
    gimimo_data_str = gimimo_data.strftime("%y%m%d")
    # Likusios skaitmenys yra unikalus numeris
    unikalus_nr_str = str(eiles_nr).zfill(4)
    return str(pirmas_skaitmuo) + gimimo_data_str + unikalus_nr_str
