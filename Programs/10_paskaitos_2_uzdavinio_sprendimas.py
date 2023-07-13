import sqlite3

# Sukuriame duombaze
conn = sqlite3.connect('10_paskaitos.db')

# 1 variantas be with

# Sukuriame lentele
conn.execute('''CREATE TABLE IF NOT EXISTS PASKAITOS
                (PAVADINIMAS TEXT NOT NULL,
                DESTYTOJAS TEXT NOT NULL,
                TRUKME INT NOT NULL);''')

# Sukuriam paskaitas
paskaitos = [('Vadyba', 'Domantas', 40),
              ('Python', 'Donatas', 80),
              ('Java', 'Tomas', 80)]
conn.executemany("INSERT INTO PASKAITOS (PAVADINIMAS, DESTYTOJAS, TRUKME) VALUES (?, ?, ?)", paskaitos)

conn.commit()

# Atspausdiname paskaitas, kuriu trukme didesne nei 50
cursor = conn.execute("SELECT * from PASKAITOS where TRUKME > 50")
print("Paskaitos, kuriu trukme didesne nei 50:")
for row in cursor:
    print("Pavadinimas = ", row[0])
    print('Destytojas = ', row[1])
    print("Trukme = ", row[2], "\n")

# Atnaujinaname paskaitos "Python" pavadinima
conn.execute("UPDATE PASKAITOS set PAVADINIMAS = 'Python programavimas' where PAVADINIMAS = 'Python'")
conn.commit()

# Istriname paskaita kuriai desto 'Tomas'
conn.execute("DELETE from PASKAITOS where DESTYTOJAS = 'Tomas'")
conn.commit()

# Atspausdiname visas paskaitas
cursor = conn.execute("SELECT * from PASKAITOS")
print("Visos paskaitos:")
for row in cursor:
    print("Pavadinimas = ", row[0])
    print('Destytojas = ', row[1])
    print("Trukme = ", row[2], "\n")

# Uzdarome duomenu baze
conn.close()

# 2 variantas su with

# Sukuriame duombaze
conn = sqlite3.connect('10_paskaitos.db')

# Sukuriame kursoriu
c = conn.cursor()

# Sukuriame lentele
with conn:
    c.execute('''CREATE TABLE IF NOT EXISTS PASKAITOS
                (PAVADINIMAS TEXT NOT NULL,
                DESTYTOJAS TEXT NOT NULL,
                TRUKME INT NOT NULL);''')

# Sukuriam paskaitas
paskaitos = [('Vadyba', 'Domantas', 40),
              ('Python', 'Donatas', 80),
              ('Java', 'Tomas', 80)]
with conn:
    c.executemany("INSERT INTO PASKAITOS (PAVADINIMAS, DESTYTOJAS, TRUKME) VALUES (?, ?, ?)", paskaitos)
    # c.commit()

# Atspausdiname paskaitas, kuriu trukme didesne nei 50
cursor = conn.execute("SELECT * from PASKAITOS where TRUKME > 50")
print("Paskaitos, kuriu trukme didesne nei 50:")
for row in cursor:
    print("Pavadinimas = ", row[0])
    print('Destytojas = ', row[1])
    print("Trukme = ", row[2], "\n")

# Atnaujinaname paskaitos "Python" pavadinima
with conn:
    c.execute("UPDATE PASKAITOS set PAVADINIMAS = 'Python programavimas' where PAVADINIMAS = 'Python'")
    # c.commit()

# Istriname paskaita kuriai desto 'Tomas'
with conn:
    c.execute("DELETE from PASKAITOS where DESTYTOJAS = 'Tomas'")
    # c.commit()

# Atspausdiname visas paskaitas
cursor = conn.execute("SELECT * from PASKAITOS")
print("Visos paskaitos:")
for row in cursor:
    print("Pavadinimas = ", row[0])
    print('Destytojas = ', row[1])
    print("Trukme = ", row[2], "\n")

# Uzdarome duomenu baze
conn.close()
