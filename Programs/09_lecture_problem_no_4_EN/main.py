from biudzetas import Biudzetas
from pajamu_irasas import PajamuIrasas
from islaidu_irasas import IslaiduIrasas

biudzetas = Biudzetas()

# Add a revenue record
pajamu_irasas = PajamuIrasas(1000, 'Jonas', 'Alga')
biudzetas.prideti_irasa(pajamu_irasas)

# Add an expense record
islaidu_irasas = IslaiduIrasas(500, 'Grynais', 'Maistas')
biudzetas.prideti_irasa(islaidu_irasas)

print(biudzetas.gauti_balansa())
print(biudzetas.gauti_ataskaita())
