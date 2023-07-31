import tkinter as tk
from tkinter import messagebox
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///employees.db', echo = True)
Base = declarative_base()

# Sukuriame duomenų bazės modelį
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    dob = Column(Date)
    position = Column(String)
    salary = Column(Float)
    start_date = Column(Date)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def main_window():
    window = tk.Tk()
    window.title("Employee Database")

    tk.Label(window, text="Name: ").grid(row=0)
    tk.Label(window, text="Surname: ").grid(row=1)
    tk.Label(window, text="Position: ").grid(row=2)
    tk.Label(window, text="Salary: ").grid(row=3)

    name = tk.Entry(window)
    surname = tk.Entry(window)
    position = tk.Entry(window)
    salary = tk.Entry(window)

    name.grid(row=0, column=1)
    surname.grid(row=1, column=1)
    position.grid(row=2, column=1)
    salary.grid(row=3, column=1)

    tk.Button(window, text='Quit', command=window.quit).grid(row=4, column=0, sticky=tk.W, pady=4)
    tk.Button(window, text='Add', command=lambda: add_employee_gui(name.get(), surname.get(), position.get(), salary.get())).grid(row=4, column=1, sticky=tk.W, pady=4)
    tk.Button(window, text='View', command=view_employees_gui).grid(row=4, column=2, sticky=tk.W, pady=4)
    tk.Button(window, text='Delete', command=lambda: delete_employee_gui(int(salary.get()))).grid(row=4, column=3, sticky=tk.W, pady=4)
    tk.Button(window, text='Update', command=lambda: update_employee_gui(int(salary.get()), name.get(), surname.get(), position.get(), salary.get())).grid(row=4, column=4, sticky=tk.W, pady=4)

    window.mainloop()

# Funkcija, kuri prideda naują asmenį į duomenų bazę
def add_employee_gui(name, surname, position, salary):
    dob = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
    start_date = datetime.now().date()
    new_employee = Employee(name=name, surname=surname, dob=dob, position=position, salary=float(salary), start_date=start_date)
    session.add(new_employee)
    session.commit()
    messagebox.showinfo("Information","Employee Added Successfully")

# Funkcija, kuri rodo visus asmenis duomenų bazėje
def view_employees_gui():
    employees = session.query(Employee).all()
    emp_str = ""
    for employee in employees:
        emp_str += f"ID: {employee.id}, Name: {employee.name}, Surname: {employee.surname}, Position: {employee.position}, Salary: {employee.salary}\n"
    messagebox.showinfo("Employees", emp_str)

# Funkcija, kuri ištrina pasirinktą asmenį iš duomenų bazės
def delete_employee_gui(id):
    try:
        employee = session.query(Employee).get(id)
        session.delete(employee)
        session.commit()
        messagebox.showinfo("Information","Employee Deleted Successfully")
    except NoResultFound:
        messagebox.showinfo("Error","Employee Not Found")

# Funkcija, kuri pakeičia pasirinktą asmenį duomenų bazėje
def update_employee_gui(id, name, surname, position, salary):
    try:
        employee = session.query(Employee).get(id)
        employee.name = name
        employee.surname = surname
        employee.position = position
        employee.salary = float(salary)
        session.commit()
        messagebox.showinfo("Information","Employee Updated Successfully")
    except NoResultFound:
        messagebox.showinfo("Error","Employee Not Found")

if __name__ == "__main__":
    main_window()
