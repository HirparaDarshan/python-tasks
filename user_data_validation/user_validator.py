""" Task 3 : Validate username and password using lambda """

# Username validation lambdas
length_check = lambda username: len(username) >= 8
dot_check = lambda username: '.' in username
underscore_check = lambda username: '_' in username
alphanumeric_check = lambda username: any(char.isalpha() for char in username)

# Password validation lambdas
special_check = lambda password: any(char in "@,#,$,%" for char in password)
uppercase_check = lambda password: any(char.isupper() for char in password)
lowercase_check = lambda password: any(char.islower() for char in password)
digits_check = lambda password: any(char.isdigit() for char in password)

# Validate Username
while True:
    username = input("Enter Username : ")
    IS_VALID = True

    if not length_check(username):
        print("Username must be 8 characters long.")
        IS_VALID = False

    if not dot_check(username):
        print("Username must contain a dot '.'")
        IS_VALID = False

    if not underscore_check(username):
        print("Username must contain an underscore'_'")
        IS_VALID = False

    if not alphanumeric_check(username):
        print("Usernam must contain atleast one alphabet")
        IS_VALID = False

    if IS_VALID :
        print("username is valid")
        break

# Validate Password
while True:
    password = input("Enter Password : ")
    IS_VALID = True

    if not length_check(password):
        print("Password must be 8 characters long.")
        IS_VALID = False

    if not special_check(password):
        print("password must contain any of these special characters '@#$%'")
        IS_VALID = False

    if not uppercase_check(password):
        print("password must contain atleast one uppercase character")
        IS_VALID = False

    if not lowercase_check(password):
        print("password must contain atleat one lowercase character")
        IS_VALID = False

    if not digits_check(password):
        print("password must have atleast one digit")
        IS_VALID = False

    if IS_VALID :
        print("Password is valid")
        break
