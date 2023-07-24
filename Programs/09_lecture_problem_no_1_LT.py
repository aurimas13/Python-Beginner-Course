# Importuoti modulį datetime.
import datetime

# Atsispausdinti šiandienos datą ir laiką kartu.
print(datetime.datetime.now())

# Atsispausdinti tik datą.
print(datetime.date.today())

# Atsispausdinti tik laiką.
print(datetime.datetime.now().time())

# Iš paketo datetime importuoti modulį date.
from datetime import date

# Atsispausdinti šiandienos datą.
print(date.today())

# Iš paketo datetime importuoti modulį date kaip data.
from datetime import date as data

# Atsispausdinti šiandienos datą.
print(data.today())
