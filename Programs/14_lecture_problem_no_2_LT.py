# Need pip install SQLAlchemy and pip install tk 
# to run first before executing this code


import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Sukuriame duomenų bazės modelį
class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)
    # Galite pridėti daugiau laukų, jei reikia

# Sukuriame duomenų bazės objektą ir sesiją
engine = create_engine('sqlite:///persons.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Funkcija, kuri prideda naują asmenį į duomenų bazę
def add_person():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    age = int(entry_age.get())
    
    person = Person(first_name=first_name, last_name=last_name, age=age)
    session.add(person)
    session.commit()
    messagebox.showinfo("Informacija", "Asmuo pridėtas sėkmingai.")
    clear_entries()
    show_persons()

# Funkcija, kuri rodo visus asmenis duomenų bazėje
def show_persons():
    persons_list.delete(0, tk.END)
    persons = session.query(Person).all()
    for person in persons:
        persons_list.insert(tk.END, f"{person.first_name} {person.last_name} ({person.age} m.)")

# Funkcija, kuri ištrina pasirinktą asmenį iš duomenų bazės
def delete_person():
    selected_index = persons_list.curselection()
    if selected_index:
        selected_person = persons_list.get(selected_index)
        first_name, last_name, _ = selected_person.split(" ")
        person = session.query(Person).filter_by(first_name=first_name, last_name=last_name).first()
        if person:
            session.delete(person)
            session.commit()
            messagebox.showinfo("Informacija", "Asmuo ištrintas sėkmingai.")
            show_persons()

# Funkcija, kuri išvalo įvedimo laukus
def clear_entries():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

# Sukuriame Tkinter langą
root = tk.Tk()
root.title("Asmenų valdymo programa")
root.geometry("400x300")

# Sukuriame etiketes
label_first_name = tk.Label(root, text="Vardas:")
label_last_name = tk.Label(root, text="Pavardė:")
label_age = tk.Label(root, text="Amžius:")

# Sukuriame įvedimo laukus
entry_first_name = tk.Entry(root)
entry_last_name = tk.Entry(root)
entry_age = tk.Entry(root)

# Sukuriame mygtukus
button_add = tk.Button(root, text="Pridėti", command=add_person)
button_delete = tk.Button(root, text="Ištrinti", command=delete_person)

# Sukuriame sąrašo langą
persons_list = tk.Listbox(root, width=50)

# Sudedame elementus į langą
label_first_name.pack(pady=5)
entry_first_name.pack(pady=5)
label_last_name.pack(pady=5)
entry_last_name.pack(pady=5)
label_age.pack(pady=5)
entry_age.pack(pady=5)
button_add.pack(pady=5)
button_delete.pack(pady=5)
persons_list.pack(pady=5)

# Parodome esamus asmenis
show_persons()

# Paleidžiame Tkinter programos ciklą
root.mainloop()
