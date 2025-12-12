""" Task 8: Taking user time and performing different operation on it """
from datetime import datetime, time

def get_user_time(time_msg):
    """
    Prompts the user for a time in HH:MM:SS format.
    """
    while True:
        time_str = input(time_msg)
        try:
            time_obj = datetime.strptime(time_str, "%H:%M:%S").time()
            return time_obj
        except ValueError:
            print("Invalid time format. Please use HH:MM:SS.\n")

def time_to_sec(time_value):
    """
    Converts time value to total seconds
    """
    return time_value.hour * 3600 + time_value.minute * 60 + time_value.second

def sec_to_time(total_seconds):
    """
    Convert seconds back to datetime
    """
    seconds_in_day = total_seconds % 86400

    hours_in = seconds_in_day // 3600
    minutes_in = (seconds_in_day % 3600) // 60
    seconds_in = seconds_in_day % 60

    return time(hour=hours_in, minute=minutes_in, second=seconds_in)

# *** Main Program starts here ***
user_time = get_user_time("Enter time in HH:MM:SS format: ")
print(f"You entered the time: {user_time} \n")

while True:
    print("Choose an operation:")
    print("1: Increase time (add duration)")
    print("2: Add a new time to the base time")
    print("3: Find the difference between base time and a new time")
    print("4: To exit \n")
    user_choice = input("Enter the number of your choice (1, 2, 3 or 4): ")

    if user_choice == "1":

        try:
            hours = int(input("Add hours: "))
            minutes = int(input("Add minutes: "))
            seconds = int(input("Add seconds: "))

            old_time_seconds = time_to_sec(user_time)
            seconds_to_add = hours * 3600 + minutes * 60 + seconds

            new_total_sec = old_time_seconds + seconds_to_add
            user_time = sec_to_time(new_total_sec)

            print(f"New time after increament is {user_time}\n")
        except ValueError:
            print("Invalid number input. Please enter integers for H/M/S.\n")

    elif user_choice == "2":

        add_time = get_user_time("Enter time to add in HH:MM:SS format : ")

        old_time_seconds = time_to_sec(user_time)
        add_time_seconds = time_to_sec(add_time)

        combined_seconds = old_time_seconds + add_time_seconds

        combined_time = sec_to_time(combined_seconds)

        print(f"New time after additon is {combined_time}\n")

    elif user_choice == "3":

        new_time = get_user_time("Please enter new time in HH:MM:SS format: ")

        old_time_seconds = time_to_sec(user_time)
        new_time_seconds = time_to_sec(new_time)

        difference_seconds = abs(old_time_seconds - new_time_seconds)

        hours = difference_seconds // 3600
        minutes = (difference_seconds % 3600) // 60
        seconds = difference_seconds % 60

        format_difference = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        print(f"The difference between the two times is: {format_difference}\n")

    elif user_choice == "4":
        break

    else:
        print("Invalid input! select from (1,2,3 or 4) \n")
