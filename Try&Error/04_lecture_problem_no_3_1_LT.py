# Funkcija, kuri patikrina ar pirmoji pusė skaičiaus yra lygi antroji
def ar_lygios_puses(skaicius):
    skaicius_str = str(skaicius)  # Konvertuojame skaičių į stringą, kad galėtume dirbti su skaitmenimis
    pusiu_ilgis = len(skaicius_str) // 2  # Randame pusę skaičiaus

    # Jei skaičius yra nelyginis, negalime tiesiogiai palyginti puses
    if len(skaicius_str) % 2 != 0:
        return False
    
    # Palyginame pirmąją ir antrąją puses
    return skaicius_str[:pusiu_ilgis] == skaicius_str[pusiu_ilgis:]

# Funkcija, kuri grąžina gretimus skaičius
def gretimi_skaiciai(skaicius):
    skaicius_str = str(skaicius)  # Konvertuojame skaičių į stringą, kad galėtume dirbti su skaitmenimis
    rezultatas = []  # Čia saugosime rezultatus

    # Einame per kiekvieną skaitmenį skaičiuje
    for i in range(len(skaicius_str)):
        # Jei tai pirmas skaitmuo, gretimas yra pats skaitmuo ir sekantis
        if i == 0:
            gretimas = skaicius_str[i] + skaicius_str[i+1]
        # Jei tai paskutinis skaitmuo, gretimas yra pats skaitmuo ir ankstesnis
        elif i == len(skaicius_str) - 1:
            gretimas = skaicius_str[i-1] + skaicius_str[i]
        # Kitu atveju gretimi yra ankstesnis ir sekantis skaitmenys
        else:
            gretimas = skaicius_str[i-1] + skaicius_str[i] + skaicius_str[i+1]

        rezultatas.append(f"{skaicius_str[i]} – {gretimas}")  # Pridedame rezultatą prie sąrašo

    return rezultatas
