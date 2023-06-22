class Sentence:
    def __init__(self, text="default"):  # Use a default text if no text is provided
        self.text = text

    def reverse_text(self):  # Method to return the text in reverse
        return self.text[::-1]

    def to_lowercase(self):  # Method to return the text in lowercase
        return self.text.lower()

    def to_uppercase(self):  # Method to return the text in uppercase
        return self.text.upper()

    def get_word_by_index(self, index):  # Method to return a word by its order number in the sentence
        words = self.text.split()  # Split the text into words
        if index < len(words):  # Check if the index is within the range
            return words[index]  # Return the word at the given index
        return "Index out of range"  # Return an error message if index is out of range

    def count_occurrences(self, item):  # Method to return the count of a specified character or word in the text
        return self.text.count(item)

    def replace_item(self, old_item, new_item):  # Method to return the text with a specified word or character replaced
        return self.text.replace(old_item, new_item)

    def print_info(self):  # Method to print the number of words, numbers, uppercase and lowercase letters in the sentence
        words = len(re.findall(r'\b\w+\b', self.text))  # Count the words
        numbers = len(re.findall(r'\b\d+\b', self.text))  # Count the numbers
        uppercase = len(re.findall(r'[A-Z]', self.text))  # Count the uppercase letters
        lowercase = len(re.findall(r'[a-z]', self.text))  # Count the lowercase letters

        print(f"Words: {words}, Numbers: {numbers}, Uppercase: {uppercase}, Lowercase: {lowercase}")  # Print the information

# Creating and testing an object with default text
s = Sentence()
print(s.reverse_text())
print(s.to_lowercase())
print(s.to_uppercase())
print(s.get_word_by_index(1))
print(s.count_occurrences('a'))
print(s.replace_item('a', 'b'))
s.print_info()
