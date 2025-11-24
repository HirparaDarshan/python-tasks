""" Task 2: Modify User Paragraph """

user_input = input("Enter a paragraph: ")
split_input = user_input.split()


def confirm_edit(msg):
    """ Function to validate yes/no input """

    while True:
        user_response = input(msg).lower()
        if user_response in ["yes", "no"]:
            return user_response
        print("Invalid input. Please enter 'yes' or 'no'.")


def validate_input(msg):
    """ Function to get a valid word to edit or delete """

    while True:
        word_to_edit = input(msg)
        if word_to_edit in split_input:
            return word_to_edit
        print("Word not found in the paragraph. try again.")

# Edit word in the paragraph
edit_confirmation = confirm_edit("Do you want to edit any word? (yes/no): ")

if edit_confirmation == 'yes':
    edit_choice = validate_input("Enter the word you want to edit: ")
    if edit_choice in split_input:
        new_word = input("Enter the new word: ")
        index = split_input.index(edit_choice)
        split_input[index] = new_word
        print("Updated paragraph:", ' '.join(split_input))

# Delete word from the paragraph
delete_confirmation = confirm_edit("do you want to delete any word? (yes/no): ")

if delete_confirmation == 'yes':
    delete_choice = validate_input("Enter the word you want to delete: ")
    if delete_choice in split_input:
        split_input.remove(delete_choice)
        print("Updated paragraph:", ' '.join(split_input))
