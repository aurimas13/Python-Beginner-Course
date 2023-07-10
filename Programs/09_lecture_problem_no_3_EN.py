# main.py
from modules.python_kursas import PythonKursas
from modules.kursas import Kursas

# Initialize a Kursas object with desired properties
kursas_obj = Kursas('Kursas Pavadinimas', 'Destytojas', 10)

# Initialize a PythonKursas object with desired properties
python_kursas_obj = PythonKursas('Python Kursas', 'Python Destytojas', 20)

# Call the destyti() method for both objects
kursas_obj.destyti()
python_kursas_obj.destyti()



