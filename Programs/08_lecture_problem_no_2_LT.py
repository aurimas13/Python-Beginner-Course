from statistics import mean, median

# Step 1: Create a list of numbers from 0 to 50.
numbers = list(range(51))

# Step 2: Multiply all numbers in the list by 10 and print them.
multiplied_by_10 = list(map(lambda x: x * 10, numbers))
print("Numbers multiplied by 10:", multiplied_by_10)

# Step 3: Select numbers that are divisible by 7 and print them.
divisible_by_7 = list(filter(lambda x: x % 7 == 0, multiplied_by_10))
print("Numbers divisible by 7:", divisible_by_7)

# Step 4: Square all the numbers in the list and print them.
squared_numbers = [x**2 for x in multiplied_by_10]
print("Squared numbers:", squared_numbers)

# Step 5: Perform the following actions with the list of squares:
# print the sum, the smallest and largest number, the average, and the median.
print("Sum of squares:", sum(squared_numbers))
print("Min of squares:", min(squared_numbers))
print("Max of squares:", max(squared_numbers))
print("Mean of squares:", mean(squared_numbers))
print("Median of squares:", median(squared_numbers))

# Step 6: Sort and print the list of squares in reverse order.
sorted_squares_desc = sorted(squared_numbers, reverse=True)
print("Squares sorted in descending order:", sorted_squares_desc)
