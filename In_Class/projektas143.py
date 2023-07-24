from projektas141 import Projektas
from projektas142 import session

# projektas1 = session.query(Projektas).get(1)
projektas1 = session.get(Projektas, 1)
print(projektas1)

projektas2 = session.query(Projektas).filter_by(name='2_projektas').first()
print(projektas2)

projektai = session.query(Projektas).all()

for projektas in projektai:
    print(projektas.name, projektas.price)