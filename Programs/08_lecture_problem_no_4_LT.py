from operator import attrgetter

# Step 1: Create a class named Zmogus with properties vardas (name) and amzius (age).
class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius
        
    # Step 2: Implement the __repr__ method to display name and age.
    def __repr__(self):
        return f"Zmogus(vardas={self.vardas}, amzius={self.amzius})"

# Step 3: Instantiate several Zmogus objects with names and ages.
zmogus1 = Zmogus("Jonas", 30)
zmogus2 = Zmogus("Petras", 25)
zmogus3 = Zmogus("Egle", 27)

# Step 4: Insert the created Zmogus objects into a new list.
zmogus_list = [zmogus1, zmogus2, zmogus3]

# Step 5: Sort and print the list of objects by name.
sorted_by_name = sorted(zmogus_list, key=attrgetter('vardas'))
print("Sorted by name:", sorted_by_name)

# Sort and print the list of objects by age.
sorted_by_age = sorted(zmogus_list, key=attrgetter('amzius'))
print("Sorted by age:", sorted_by_age)

# Sort and print the list of objects by name in reverse order.
sorted_by_name_reverse = sorted(zmogus_list, key=attrgetter('vardas'), reverse=True)
print("Sorted by name in reverse:", sorted_by_name_reverse)

# Sort and print the list of objects by age in reverse order.
sorted_by_age_reverse = sorted(zmogus_list, key=attrgetter('amzius'), reverse=True)
print("Sorted by age in reverse:", sorted_by_age_reverse)
