from projektas141 import Projektas
from projektas142 import session

search = session.query(Projektas).filter(Projektas.name.ilike('P%'))
search2 = session.query(Projektas).filter(Projektas.price > 10000)
search3 = session.query(Projektas).filter(
    Projektas.price > 10000,
    Projektas.name.ilike('P%'))

print([i for i in search])
print([i for i in search2])
print([i for i in search3])