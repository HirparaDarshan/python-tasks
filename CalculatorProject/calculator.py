""" Task 4 - A Calculator using Class."""

class Calculator:
    """ A Calculator class to perform basic Arithmatic, Bitwise and Comparison operations."""
    def __init__(self, num1, num2):
        """Initializes an object with two numbers."""
        self.num1 = num1
        self.num2 = num2

    """Arithmatic operation functions"""
    def addition(self):
        """Calcualte an addition of two numbers."""
        return self.num1 + self.num2

    def subtraction(self):
        """Return an subtraction of num1 - num2."""
        return self.num1 - self.num2
    
    def multiplication(self):
        """ Return a Multiplication of two numbers."""
        return self.num1 * self.num2

    def division(self):
        """ Return a division of num1 by num2 also handling division bt zero."""
        if self.num2 == 0:
            print("Cannot divide by zero")
        return self.num1 / self.num2
    
    def power(self):
        """ Return a num1 raise to the power of num2."""
        return self.num1 ** self.num2
    
    def reminder(self):
        """Returns the remainder of the division of num1 by num2."""
        return self.num1 % self.num2
    
    """Bitwise Operation Functions"""
    def bitwise_left(self):
        """Performs a bitwise left shift on num1 by num2."""
        return int(self.num1) << int(self.num2)
        
    def bitwise_right(self):
        """ Performs a bitwise right shift on num1 by num2."""
        return int(self.num1) >> int(self.num2)

    def bitwise_and(self):
        """Returns the bitwise AND of num1 and num2."""
        return int(self.num1) & int(self.num2)
    
    def bitwise_or(self):
        """Returns the bitwise OR of num1 and num2."""
        return int(self.num1) | int(self.num2)
    
    def bitwise_xor(self):
        """Returns the bitwise XOR of num1 and num2."""
        return int(self.num1) ^ int(self.num2)
    
    """Comparison operation function"""
    def less_than(self):
        """Return True if num1 is less than num2."""
        return self.num1 < self.num2
    
    def less_than_or_equal(self):
        """Return True if num1 is less than or equal to num2."""
        return self.num1 <= self.num2
    
    def equal_to(self):
        """Return True if num1 is equal to num2."""
        return self.num1 == self.num2
    
    def not_equal_to(self):
        """Return True if num1 is not equal to num2."""
        return self.num1 != self.num2
    
    def greater_than(self):
        """Return True if num1 is greater than num2."""
        return self.num1 > self.num2
    
    def greater_than_or_equal(self):
        """Return True if num1 is greater than or equal to num2."""
        return self.num1 >= self.num2
    

"""Ensures that user input can be successfully converted to a float."""
while True:
    value_1 = input("Enter Value 1 : ")
    value_2 = input("Enter value 2 : ")
    try:
        float_value1 = float(value_1)
        float_value2 = float(value_2)
        calc = Calculator(float_value1, float_value2)
        break
    except ValueError:
        print("Please input valid Number")

""" A menu-driven interface for various calculator operations using a 'match' statement."""
print("PLEASE ENTER \n"
    "1. for Addition \n"
    "2. for Subtraction \n"
    "3. for Multiplication \n"
    "4. for Division \n"
    "5. for Power \n"
    "6. for Reminder \n"
    "7. for Bitwise left \n"
    "8. for Bitwise right \n"
    "9. for Bitwise AND \n"
    "10. for Bitwise OR \n"
    "11. for Bitwise XOR \n"
    "12. for is Value 1 is less than value 2 \n"
    "13. for is Value 1 is less than or equal to value 2 \n"
    "14. for is value 1 is equal to value 2 \n"
    "15. for is value 1 is not equal to value 2 \n"
    "16. for is value 1 is greater than value 2 \n"
    "17. for is value 1 is greater than or equal to value 2 \n"
    "18. for Exit \n"
    )
while True:
    user_choice = input("Enter your choice : ")

    match user_choice:
        case "1":
            print("The Addition is :", calc.addition())
        case "2":
            print("The Subtraction is :", calc.subtraction())
        case "3":
            print("The Multiplication is :", calc.multiplication())
        case "4":
            print("The Division is :", calc.division())
        case "5":
            print("The Power is :", calc.power())
        case "6":
            print("The reminder :", calc.reminder())
        case "7":
            print("The bitwise left is :", calc.bitwise_left())
        case "8":
            print("The bitwise right is :", calc.bitwise_right())
        case "9":
            print("The bitwise AND is :", calc.bitwise_and())
        case "10":
            print("The bitwise OR is :", calc.bitwise_or())
        case "11":
            print("The bitwie XOR is :", calc.bitwise_xor())
        case "12":
            print("Value 1 is less than value 2 :", calc.less_than())
        case "13":
            print("Value 1 is less than or equal to value 2 :", calc.less_than_or_equal())
        case "14":
            print("Value 1 is equal to value 2 :", calc.equal_to())
        case "15":
            print("Value 1 is not equal to value 2 :", calc.not_equal_to())
        case "16":
            print("Value 1 is greater than value 2 :", calc.greater_than())
        case "17":
            print("Value 1 is greater than or equal to value 2 :", calc.greater_than_or_equal())
        case "18":
            break
        case _:
            print("Invalid day number.")
