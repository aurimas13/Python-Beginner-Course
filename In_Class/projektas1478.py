from projektas141 import Projektas
from projektas142 import engine, session
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("""Pasirinkite veiksma:
                             1. Atvaizduoti visus projektus
                             2. Sukurti nauja projekta
                             3. Pakeisti projekta
                             4. Istrinti projekta\n"""))
    if pasirinkimas == 1:
        projektai = session.query(Projektas).all()
        print("--------------------------------")
        for projektas in projektai:
            print(projektas)  
        print("--------------------------------")

    if pasirinkimas == 2:
        name = input("Iveskite projekto pavadinima: ")
        price = input("Iveskite projekto kaina: ")
        projektas = Projektas(name=name, price=price)
        session.add(projektas)
        session.commit()

    if pasirinkimas == 3:
        projektai = session.query(Projektas).all()
        print("--------------------------------")
        for projektas in projektai:
            print(projektas) 
        print("--------------------------------")
        keiciamo_id = int(input("Iveskite projekto ID, kuri norite pakeisti: "))
        keiciamas_projektas = session.query(Projektas).get(keiciamo_id)
        pakeitimas = int(input("Ka norite pakeisti? 1 - pavadinima, 2 - kaina: "))
        if pakeitimas == 1:
            keiciamas_projektas.name = input("Iveskite nauja pavadinima: ")
        if pakeitimas == 2:
            keiciamas_projektas.price = input("Iveskite nauja kaina: ")
        session.commit()

    if pasirinkimas == 4:
        projektai = session.query(Projektas).all()
        print("--------------------------------")
        for projektas in projektai:
            print(projektas) 
        print("--------------------------------")
        trinamo_id = int(input("Iveskite projekto ID, kuri norite istrinti: "))
        trinamas_projektas = session.query(Projektas).get(trinamo_id)
        session.delete(trinamas_projektas)
        session.commit()    
