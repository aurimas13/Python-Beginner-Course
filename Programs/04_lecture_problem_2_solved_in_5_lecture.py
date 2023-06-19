import datetime


# Funckija patikrinanti asmens kodo validumą
def ar_validus_asmens_kodas(kodas):
    """Patikrina ar paduotas asmens kodas yra validus"""
    # Asmens kodas turi būti 11 skaitmenų ilgio
    if len(kodas) != 11:
        return False
    # Pirmas skaitmuo nurodo lyti ir gimimo simtmeti
    lytis_gimimo_simtemetyje = int(kodas[0])
    if lytis_gimimo_simtemetyje < 1 or lytis_gimimo_simtemetyje > 6:
        return False
    #Kiti sesi skaitmenys nurodo gimimo data:
    try:
        datetime.datetime.strptime(kodas[1:7], "%y%m%d")
    except ValueError:
        return False
    # Likusieji skitmenys yra uniklaus numeri, kuris prival buti didesnis uz 0
    if int(kodas[7:]) <= 0:
        return False
    return True

# Funkcija kuri generuoja asmens koda
def generuoti_asmens_koda(lytis, gimimo_data, eiles_nr):
    """Generuoja asmens koda pagal ivesta lyti, gimimo data ir eiles numeri"""
    # Pirmas skaitmuo nurodo lyti ir gimimo simtmeti
    if int(gimimo_data[:2]) < 19:
        pirmas_skaitmuo = 1 if lytis == "vyras" else 2
    elif int(gimimo_data[:2]) < 20:
        pirmas_skaitmuo = 3 if lytis == "vyras" else 4
    else:
        pirmas_skaitmuo = 5 if lytis == "vyras" else 6
    # Kiti sesi skaitmenys nurodo gimimo data:
        gimimo_data_obj = datetime.datetime.strptime(gimimo_data, "%y%m%d")
        gimimo_data_str = gimimo_data_obj.strftime("%y%m%d")
    # Liki skaimenys yra unikalus numeris
        unikalus_nr_str = str(eiles_nr).zfill(4)
    return str(pirmas_skaitmuo) + gimimo_data_str + unikalus_nr_str


if __name__ == "__main__":
    print(ar_validus_asmens_kodas("48904040404"))
    print(generuoti_asmens_koda("vyras", "200606", "1789"))