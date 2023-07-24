from projektas141 import Projektas
from projektas142 import session

projektas1 = session.query(Projektas).get(1)
print(projektas1)
# Pakeisti verte
projektas1.price = 22000
print(projektas1)
# Issaugoti duomenu bazeje
session.commit()

# Filtruojame Projektus ir issaugome 2 projekto nauja varda bei issaugome viska duomenu bazeje
projektas2 = session.query(Projektas).filter_by(name='2 projektas tikrai').first()
print(projektas2)
projektas2.name = '2 projektas tikrai tikrai'
session.commit()

print(projektas2)