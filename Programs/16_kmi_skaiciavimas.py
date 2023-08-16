# kmi_skaiciavimas.py

def kmi(mass, height):
    """
    Ši funkcija skaičiuoja kūno masės indeksą (KMI).

    :param mass: Žmogaus svoris kilogramais.
    :param height: Žmogaus ūgis metrais.
    :return: Grąžina KMI.
    """

    # Patikriname, ar svoris ir ūgis yra normaliomis ribomis.
    if mass < 30 or masss > 200 or height < 1.0 or height > 2.5:
        raise ValueError("Netinkami duomenys")

    return mass / (height ** 2)
