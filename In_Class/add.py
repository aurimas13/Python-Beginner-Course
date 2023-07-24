from projektas141 import Projektas
from projektas142 import session

# Create new instances of the Projektas
projektas1 = Projektas("Projektas1", 100.5)
projektas2 = Projektas("Projektas2", 200.5)
projektas3 = Projektas("Projektas3", 20000.0)
projektas4 = Projektas("Projektas4", 55000.0)

# Add new Projektas instances to the session
session.add(projektas1)
session.add(projektas2)
session.add(projektas3)
session.add(projektas4)

# Commit the session to the database
session.commit()