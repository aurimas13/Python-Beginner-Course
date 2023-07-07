# Given list
sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# Step 2: Calculate and print the sum of all the numbers in the list.
# Note: In Python, boolean True is also considered as 1 when performing arithmetic calculations.
numbers = [x for x in sarasas if isinstance(x, (int, float))]
sum_of_numbers = sum(numbers)
print("Sum of all numbers:", sum_of_numbers)

# Step 3: Concatenate and print all the words in the list.
words = [x for x in sarasas if isinstance(x, str)]
concatenated_words = " ".join(words)
print("Concatenated words:", concatenated_words)

# Step 4: Count and print how many boolean variables in the list have the value True.
true_count = sum(1 for x in sarasas if isinstance(x, bool) and x is True)
print("Count of boolean True values:", true_count)
