# Need pip install SQLAlchemy to run first before executing this code

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Sukuriame darbuotojo modelį
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    birth_date = Column(Date)
    position = Column(String(50))
    salary = Column(Float)
    hire_date = Column(DateTime, default=datetime.now)

# Sukuriame duomenų bazės objektą ir sesiją
engine = create_engine('sqlite:///employees.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Funkcija, kuri leidžia įvesti darbuotoją
def add_employee():
    first_name = input("Įveskite darbuotojo vardą: ")
    last_name = input("Įveskite darbuotojo pavardę: ")
    birth_date = input("Įveskite darbuotojo gimimo datą (pvz. 1990-01-01): ")
    position = input("Įveskite darbuotojo pareigas: ")
    salary = float(input("Įveskite darbuotojo atlyginimą: "))

    # Sukuriame naują darbuotojo objektą ir pridedame į sesiją
    employee = Employee(first_name=first_name, last_name=last_name, birth_date=birth_date,
                        position=position, salary=salary)
    session.add(employee)
    session.commit()
    print("Darbuotojas sėkmingai pridėtas.")

# Funkcija, kuri leidžia peržiūrėti visus darbuotojus
def view_employees():
    employees = session.query(Employee).all()
    for employee in employees:
        print(f"{employee.first_name} {employee.last_name} ({employee.position}): {employee.salary}")

# Funkcija, kuri leidžia ištrinti darbuotoją
def delete_employee():
    employee_id = int(input("Įveskite darbuotojo ID, kurį norite ištrinti: "))
    employee = session.query(Employee).filter_by(id=employee_id).first()
    if employee:
        session.delete(employee)
        session.commit()
        print("Darbuotojas sėkmingai ištrintas.")
    else:
        print("Darbuotojas su nurodytu ID nerastas.")

# Funkcija, kuri leidžia atnaujinti darbuotojo informaciją
def update_employee():
    employee_id = int(input("Įveskite darbuotojo ID, kurį norite atnaujinti: "))
    employee = session.query(Employee).filter_by(id=employee_id).first()
    if employee:
        first_name = input(f"Įveskite naują vardą ({employee.first_name}): ")
        last_name = input(f"Įveskite naują pavardę ({employee.last_name}): ")
        birth_date = input(f"Įveskite naują gimimo datą ({employee.birth_date}): ")
        position = input(f"Įveskite naujas pareigas ({employee.position}): ")
        salary = float(input(f"Įveskite naują atlyginimą ({employee.salary}): "))

        employee.first_name = first_name if first_name else employee.first_name
        employee.last_name = last_name if last_name else employee.last_name
        employee.birth_date = birth_date if birth_date else employee.birth_date
        employee.position = position if position else employee.position
        employee.salary = salary if salary else employee.salary

        session.commit()
        print("Darbuotojo informacija sėkmingai atnaujinta.")
    else:
        print("Darbuotojas su nurodytu ID nerastas.")

# Pagrindinė programa
if __name__ == "__main__":
    while True:
        print("\nMeniu:")
        print("1. Pridėti darbuotoją")
        print("2. Peržiūrėti visus darbuotojus")
        print("3. Ištrinti darbuotoją")
        print("4. Atnaujinti darbuotojo informaciją")
        print("5. Baigti")

        choice = input("Pasirinkite veiksmą (1-5): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")
