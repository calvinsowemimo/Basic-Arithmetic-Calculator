# Import Tkinter for GUI creation
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox

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

# Memory file path
memory_file = "calculator_memory.txt"

# Memory functions
def add_to_memory():
    """Save the current result to a memory file."""
    try:
        with open(memory_file, "w") as file:
            file.write(result.get())
    except Exception as e:
        messagebox.showerror("Error", "Failed to save memory.")

def recall_memory():
    """Load and display the saved value from memory."""
    try:
        with open(memory_file, "r") as file:
            memory_value = file.read()
            number1.set(memory_value)
    except FileNotFoundError:
        messagebox.showinfo("Info", "Memory is empty.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to read memory.")

def clear_memory():
    """Clear the stored value in the memory file."""
    try:
        open(memory_file, "w").close()
    except Exception as e:
        messagebox.showerror("Error", "Failed to clear memory.")

# Initialize the main window
root = Tk()
root.title("Colorful Calculator for Kids")
root.configure(bg='light blue')

# Initialize string variables for storing input and result
number1 = StringVar()
number2 = StringVar()
result = StringVar()

# GUI widgets setup
Label(root, text="Number 1:", bg='light blue', font=('Helvetica', 12)).grid(row=0, column=0, sticky="w")
Entry(root, textvariable=number1, bg='white').grid(row=0, column=1)
Label(root, text="Number 2:", bg='light blue', font=('Helvetica', 12)).grid(row=1, column=0, sticky="w")
Entry(root, textvariable=number2, bg='white').grid(row=1, column=1)
Button(root, text="+", command=add, bg='light green', font=('Helvetica', 12)).grid(row=2, column=0)
Button(root, text="-", command=subtract, bg='salmon', font=('Helvetica', 12)).grid(row=2, column=1)
Button(root, text="*", command=multiply, bg='yellow', font=('Helvetica', 12)).grid(row=3, column=0)
Button(root, text="/", command=divide, bg='orange', font=('Helvetica', 12)).grid(row=3, column=1)
Label(root, text="Result:", bg='light blue', font=('Helvetica', 12)).grid(row=4, column=0, sticky="w")
Label(root, textvariable=result, bg='light blue', font=('Helvetica', 12)).grid(row=4, column=1, sticky="w")

# Memory function buttons
Button(root, text="M+", command=add_to_memory, bg='cyan', font=('Helvetica', 12)).grid(row=5, column=0)
Button(root, text="MRC", command=recall_memory, bg='cyan', font=('Helvetica', 12)).grid(row=5, column=1)
Button(root, text="MC", command=clear_memory, bg='cyan', font=('Helvetica', 12)).grid(row=5, column=2)

root.mainloop()
