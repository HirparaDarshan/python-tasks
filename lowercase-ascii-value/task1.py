""" Task 1: Extract lowercase letters and their ASCII values"""

user_input = input("Enter any string: ")

lowercase_chars = [char for char in user_input if char.islower()]

if not lowercase_chars:
    print("No lowercase letters found")
else:
    print(''.join(lowercase_chars))
    ascii_values = [ord(char) for char in lowercase_chars]
    print("ASCII values of lowercase letters:", ascii_values)

