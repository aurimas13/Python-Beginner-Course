# Define the input text. You can replace it with your own text.
input_text = "Labas. Kaip sekasi? Vakar buvo lietus. Šiandien yra graži diena."

# Split the input text into sentences by splitting on periods, exclamation marks, and question marks.
# For this, replace all exclamation marks and question marks with periods and then split on periods.
sentences = input_text.replace('!', '.').replace('?', '.').split('.')

# Use list comprehension to create a new list of sentences with an exclamation mark added at the end of each sentence.
# We also strip any leading/trailing whitespace from each sentence.
new_sentences = [sentence.strip() + "!" for sentence in sentences if sentence.strip()]

# Combine the modified sentences into a single string with spaces in between using " ".join() and print the result.
print(" ".join(new_sentences))
