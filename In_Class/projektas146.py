from projektas141 import Projektas
from projektas142 import session

projektas1 = session.query(Projektas).filter_by(name='Projektas1').first()

session.delete(projektas1)
session.commit()

projektai = session.query(Projektas).all()

for projektas in projektai:
    print(projektas.name, projektas.price)