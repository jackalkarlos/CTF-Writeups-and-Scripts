def generate_lexicographic_wordlist(min_number, max_number):
    # Initialize an empty list to store the lexicographic numbers
    lexicographic_wordlist = []

    # Iterate through the range of numbers from min_number to max_number
    for number in range(min_number, max_number + 1):
        # Convert the number to a string and split it into a list of digits
        digits = [int(digit) for digit in str(number)]
        # Sort the digits in increasing order
        digits.sort()
        # Concatenate the digits to form a lexicographic number
        lexicographic_number = ''
        for digit in digits:
            lexicographic_number += str(digit)
        # Add the lexicographic number to the wordlist
        lexicographic_wordlist.append(lexicographic_number)

    return lexicographic_wordlist

x=int(input("Starting From: "))
y=int(input("Ending From: "))
wordlist = generate_lexicographic_wordlist(x, y)

# Write the wordlist to a text file
with open('lexicographic_numbers.txt', 'w') as file:
    for number in wordlist:
        file.write(number + '\n')
