"""Task 5 - Search and update Phone Directory including name and phone number"""

def create_phone_directory():
    """Create and return an empty phone directory."""
    return {}

def add_contact(directory, name, number):
    """Add a new contact to the phone directory."""
    name_to_add = name
    directory[name_to_add] = number

def update_contact(directory, query):
    """Search for a contact by name or number and update it."""
    results = []
    query_lower = query.lower()

    for name, number in directory.items():
        if query_lower in name.lower() or query in str(number):
            results.append((name, number))

    if results:
        print("\nSearch Results:")
        for idx, (name, number) in enumerate(results, start=1):
            print(f" {idx}. Name: {name}, Number: {number}")

        try:
            index_choice = int(
                input("Enter the index no. of the contact you want to update: ")
            )
            if 1 <= index_choice <= len(results):
                selected_name = results[index_choice - 1][0]

                update_name = input(
                    "Enter new name or press Enter to keep it same: "
                )
                if update_name:
                    directory[update_name] = directory.pop(selected_name)
                    selected_name = update_name

                try:
                    update_number = int(
                        input(f"Enter new number for {selected_name}: ")
                    )
                except ValueError:
                    print("This is not a number")
                    return

                directory[selected_name] = update_number
                print("Contact updated")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("\nNo matching contacts found.")

def list_contacts(directory):
    """List all contacts in the phone directory."""

    if not directory:
        print("\nThe directory is empty.")
        return
    for name, number in directory.items():
        print(f"Name: {name}, Number: {number}")


phone_directory = create_phone_directory()

while True:
    print("\nChoose an option: \n"
        "1. Add a new contact \n"
        "2. Search or Update a specific contact \n"
        "3. List all contacts \n"   
        "4. Exit \n"
    )

    choice = input("Enter your choice form 1 to 4: ")

    match choice:
        case "1":
            try:
                new_name = input("Enter a name : ")
                new_number = int(input("Enter a number : "))
            except ValueError:
                print("This is not a number")
            else:
                if new_name and new_number:
                    add_contact(phone_directory, new_name, new_number)
                else:
                    print("Name and number cannot be empty")
        case "2":
            user_search = input("Enter a name or a number you want to Search :")
            update_contact(phone_directory, user_search)
        case "3":
            list_contacts(phone_directory)
        case "4":
            break
        case _:
            print("\nInvalid input please try again")
