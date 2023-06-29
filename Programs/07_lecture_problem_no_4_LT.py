# Import the necessary library
import pickle
import os

# Check if the pickle file exists (i.e., if the program has been run before)
if os.path.exists('budget.pickle'):
    # If it does, load the previous budget data
    with open('budget.pickle', 'rb') as file:
        budget = pickle.load(file)
else:
    # If it doesn't, create a new empty list to store the budget data
    budget = []

while True:
    # Get the user's input
    print("Please enter an income (positive number) or expense (negative number). Enter 'q' to quit.")
    user_input = input()

    # Check if the user wants to quit
    if user_input.lower() == 'q':
        break

    # Add the user's input to the budget
    try:
        budget.append(float(user_input))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Print the current budget
    print("Current budget:", budget)

    # Calculate and print the balance
    balance = sum(budget)
    print("Current balance:", balance)

# Save the budget data for the next run of the program
with open('budget.pickle', 'wb') as file:
    pickle.dump(budget, file)
