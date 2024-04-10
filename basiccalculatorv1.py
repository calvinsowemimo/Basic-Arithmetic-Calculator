class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations like addition, subtraction,
    multiplication, division, and power calculation.
    """

    def add(self, first_number, second_number):
        """Add two numbers."""
        return first_number + second_number

    def subtract(self, first_number, second_number):
        """Subtract second number from first number."""
        return first_number - second_number

    def multiply(self, first_number, second_number):
        """Multiply two numbers."""
        return first_number * second_number

    def divide(self, first_number, second_number):
        """
        Divide first number by second number.
        Returns an error message if attempting to divide by zero.
        """
        if second_number == 0:
            return "Cannot divide by zero"
        else:
            return first_number / second_number

    def power(self, base, exponent):
        """Raise base to the power of exponent."""
        return base ** exponent

def main():
    calculator = Calculator()
    print("Welcome to the Enhanced Calculator!")

    while True:
        print("\nPlease select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ('1', '2', '3', '4', '5'):
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", calculator.add(first_number, second_number))
            elif choice == '2':
                print("Result:", calculator.subtract(first_number, second_number))
            elif choice == '3':
                print("Result:", calculator.multiply(first_number, second_number))
            elif choice == '4':
                print("Result:", calculator.divide(first_number, second_number))
            elif choice == '5':
                print("Result:", calculator.power(first_number, second_number))
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid Input. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
