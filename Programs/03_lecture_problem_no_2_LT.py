from datetime import datetime, timedelta

# Atspausdiname dabartinę datą ir laiką
dabar = datetime.now()
print("Dabartinė data ir laikas: ", dabar)

# Atimame iš dabartinės datos ir laiko 5 dienas ir juos atspausdiname
penkios_dienos_atgal = dabar - timedelta(days=5)
print("Penkios dienos atgal: ", penkios_dienos_atgal)

# Pridedame prie dabartinės datos ir laiko 8 valandas ir juos atspausdiname
astuonios_valandos_pirmyn = dabar + timedelta(hours=8)
print("Aštuonios valandos pirmyn: ", astuonios_valandos_pirmyn)

# Atspausdiname dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
print("Dabartinė data ir laikas formatu 'YYYY MM DD, HH:MM:SS': ", dabar.strftime('%Y %m %d, %H:%M:%S'))

