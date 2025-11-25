""" Task 2: Modify User Paragraph """

import re

user_input = input("Enter a Paragraph: ")

while True:
    user_choice = input("Please enter 1 to edit, 2 to delete a word, or 3 to exit: ")

    if user_choice == '1':
        edit_word = input("Enter the word you want to edit: ")
        if not edit_word or not edit_word.strip():
            print("The word to edit cannot be empty.")
        else :
            old_word = r'\b' + re.escape(edit_word) + r'\b'
            if re.search(old_word, user_input):
                new_word = input("Enter the new word: ")
                user_input = re.sub(old_word, new_word, user_input)
                print(user_input)
            else :
                print("Word not found in paragraph")

    elif user_choice == '2':
        delete_choice = input("Enter the word you want to delete: ")
        delete_word = r'\b' + re.escape(delete_choice) + r'\b'
        if re.search(delete_word, user_input):
            user_input = re.sub(delete_choice, "", user_input)
            print(user_input)
        else :
            print("Word not found in paragraph")

    elif user_choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid input. Please try again.")
