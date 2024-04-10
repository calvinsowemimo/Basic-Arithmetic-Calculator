# Import Tkinter for GUI creation
from tkinter import Tk, Label, Button, Entry, StringVar, W

# Define functions for arithmetic operations
def add():
    """Add the two entered numbers and display the result."""
    try:
        result.set(str(float(number1.get()) + float(number2.get())))
    except ValueError:
        result.set("Invalid input!")

def subtract():
    """Subtract the second number from the first and display the result."""
    try:
        result.set(str(float(number1.get()) - float(number2.get())))
    except ValueError:
        result.set("Invalid input!")

def multiply():
    """Multiply the two entered numbers and display the result."""
    try:
        result.set(str(float(number1.get()) * float(number2.get())))
    except ValueError:
        result.set("Invalid input!")

def divide():
    """Divide the first number by the second and display the result."""
    try:
        if float(number2.get()) == 0:
            result.set("Cannot divide by zero!")
        else:
            result.set(str(float(number1.get()) / float(number2.get())))
    except ValueError:
        result.set("Invalid input!")

# Initialize the main window
root = Tk()
root.title("Colorful Calculator for Kids")

# Set a playful background color
root.configure(bg='light blue')

# Initialize string variables for storing input and result
number1 = StringVar()
number2 = StringVar()
result = StringVar()

# Create and arrange the GUI widgets with added colors and font adjustments
Label(root, text="Number 1:", bg='light blue', font=('Helvetica', 12)).grid(row=0, column=0, sticky=W)
Entry(root, textvariable=number1, bg='white').grid(row=0, column=1)

Label(root, text="Number 2:", bg='light blue', font=('Helvetica', 12)).grid(row=1, column=0, sticky=W)
Entry(root, textvariable=number2, bg='white').grid(row=1, column=1)

Button(root, text="+", command=add, bg='light green', font=('Helvetica', 12)).grid(row=2, column=0)
Button(root, text="-", command=subtract, bg='salmon', font=('Helvetica', 12)).grid(row=2, column=1)
Button(root, text="*", command=multiply, bg='yellow', font=('Helvetica', 12)).grid(row=3, column=0)
Button(root, text="/", command=divide, bg='orange', font=('Helvetica', 12)).grid(row=3, column=1)

Label(root, text="Result:", bg='light blue', font=('Helvetica', 12)).grid(row=4, column=0, sticky=W)
Label(root, textvariable=result, bg='light blue', font=('Helvetica', 12)).grid(row=4, column=1, sticky=W)

# Start the GUI event loop
root.mainloop()
