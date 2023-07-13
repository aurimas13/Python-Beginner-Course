import sqlite3

# Sukurti duomenų bazę
conn = sqlite3.connect('10_paskaitos.db')

# Sukurti lentelę
conn.execute('''CREATE TABLE PASKAITOS
                 (PAVADINIMAS  TEXT    NOT NULL,
                 DESTYTOJAS    TEXT     NOT NULL,
                 TRUKME        INT     NOT NULL);''')

# Sukurti paskaitas
paskaitos = [('Vadyba', 'Domantas', 40), 
             ('Python', 'Donatas', 80), 
             ('Java', 'Tomas', 80)]
conn.executemany("INSERT INTO PASKAITOS (PAVADINIMAS,DESTYTOJAS,TRUKME) \
                  VALUES (?,?,?)", paskaitos)
conn.commit()

# Atspausdinti paskaitas, kurių trukmė didesnė už 50
cursor = conn.execute("SELECT * from PASKAITOS where TRUKME > 50")
print("Paskaitos, kurių trukmė didesnė už 50:")
for row in cursor:
   print("Pavadinimas = ", row[0])
   print("Dėstytojas = ", row[1])
   print("Trukmė = ", row[2], "\n")

# Atnaujinti paskaitos „Python“ pavadinimą
conn.execute("UPDATE PASKAITOS set PAVADINIMAS = 'Python programavimas' where PAVADINIMAS = 'Python'")
conn.commit()

# Ištrinti paskaitą, kurios dėstytojas – „Tomas“
conn.execute("DELETE from PASKAITOS where DESTYTOJAS = 'Tomas'")
conn.commit()

# Atspausdinti visas paskaitas
cursor = conn.execute("SELECT * from PASKAITOS")
print("Visos paskaitos:")
for row in cursor:
   print("Pavadinimas = ", row[0])
   print("Dėstytojas = ", row[1])
   print("Trukmė = ", row[2], "\n")

# Uždaryti duomenų bazę
conn.close()
