from pajamu_irasas import PajamuIrasas
from islaidu_irasas import IslaiduIrasas

class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_irasa(self, irasas):
        self.zurnalas.append(irasas)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            elif isinstance(irasas, IslaiduIrasas):
                balansas -= irasas.suma
        return balansas

    def gauti_ataskaita(self):
        ataskaita = ""
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                ataskaita += f"Pajamos: {irasas.suma}, Siuntejas: {irasas.siuntejas}, Info: {irasas.papildoma_informacija}\n"
            elif isinstance(irasas, IslaiduIrasas):
                ataskaita += f"Išlaidos: {irasas.suma}, Atsiskaitymo būdas: {irasas.atsiskaitymo_budas}, Prekė/Paslauga: {irasas.isigyta_preke_paslauga}\n"
        return ataskaita
