import tkinter as tk
import math
import re

# Field text for the display of numbers and operations
field_text = "1"


def add_to_field(sth):
    global field_text

    # Handle automatic multiplication when parentheses or square root is added after a number
    if field_text and field_text[-1].isdigit() and (sth == '(' or sth == '√'):
        field_text += '*'

    # Replace the last operator if a new one is added consecutively
    if field_text and field_text[-1] in '+-*/' and str(sth) in '+-*/':
        # Remove the last operator
        field_text = field_text[:-1]

    # Ensure 'sth' is treated as a string
    field_text += str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)


# Calculate function for the result
def calculate():
    global field_text
    # Function to replace '√(expression)' with sqrt(expression)
    def sqrt_replace(match):
        # Extract the content inside the parentheses
        expression = match.group(1)
        # Calculate the sqrt of the evaluated expression
        return str(math.sqrt(eval(expression)))

    # Use regex to find all instances of expression for sqrt()
    field_text_processed = re.sub(r'√\((.*?)\)', sqrt_replace, field_text)
    # Evaluate the rest of the calcul
    result = str(eval(field_text_processed))
    field.delete("1.0", "end")
    field.insert("1.0", result)



# Function to handle square root
def sqrt():
    global field_text
    # Calculate sqrt of the current field
    result = str(math.sqrt(eval(field_text)))
    field.delete("1.0", "end")
    field.insert("1.0", result)



# Function that will clear the field
def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")



# Function to remove the last character from the field
def remove_last_character():
    global field_text
    field_text = field_text[:-1]  # Remove the last character
    field.delete("1.0", "end")
    field.insert("1.0", field_text)



# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x300")



# Create the text field
field = tk.Text(window, height=2, width=21, font=("Times New Roman", 20))
field.grid(row=1, column=1, columnspan=4)



# Create the buttons to add numbers and operations
button_0 = tk.Button(window, text="0", command=lambda: add_to_field(0), width=5, font=("Times New Roman", 14))
button_0.grid(row=5, column=2)

button_1 = tk.Button(window, text="1", command=lambda: add_to_field(1), width=5, font=("Times New Roman", 14))
button_1.grid(row=4, column=1)

button_2 = tk.Button(window, text="2", command=lambda: add_to_field(2), width=5, font=("Times New Roman", 14))
button_2.grid(row=4, column=2)

button_3 = tk.Button(window, text="3", command=lambda: add_to_field(3), width=5, font=("Times New Roman", 14))
button_3.grid(row=4, column=3)

button_4 = tk.Button(window, text="4", command=lambda: add_to_field(4), width=5, font=("Times New Roman", 14))
button_4.grid(row=3, column=1)

button_5 = tk.Button(window, text="5", command=lambda: add_to_field(5), width=5, font=("Times New Roman", 14))
button_5.grid(row=3, column=2)

button_6 = tk.Button(window, text="6", command=lambda: add_to_field(6), width=5, font=("Times New Roman", 14))
button_6.grid(row=3, column=3)

button_7 = tk.Button(window, text="7", command=lambda: add_to_field(7), width=5, font=("Times New Roman", 14))
button_7.grid(row=2, column=1)

button_8 = tk.Button(window, text="8", command=lambda: add_to_field(8), width=5, font=("Times New Roman", 14))
button_8.grid(row=2, column=2)

button_9 = tk.Button(window, text="9", command=lambda: add_to_field(9), width=5, font=("Times New Roman", 14))
button_9.grid(row=2, column=3)



# Add operation buttons
button_add = tk.Button(window, text="+", command=lambda: add_to_field("+"), width=5, font=("Times New Roman", 14))
button_add.grid(row=2, column=4)

button_subtract = tk.Button(window, text="-", command=lambda: add_to_field("-"), width=5, font=("Times New Roman", 14))
button_subtract.grid(row=3, column=4)

button_multiply = tk.Button(window, text="*", command=lambda: add_to_field("*"), width=5, font=("Times New Roman", 14))
button_multiply.grid(row=4, column=4)

button_divide = tk.Button(window, text="/", command=lambda: add_to_field("/"), width=5, font=("Times New Roman", 14))
button_divide.grid(row=5, column=4)

button_sqrt = tk.Button(window, text="√", command=lambda: add_to_field("√"), width=5, font=("Times New Roman", 14))
button_sqrt.grid(row=6, column=4)

button_point = tk.Button(window, text=".", command=lambda: add_to_field("."), width=5, font=("Times New Roman", 14))
button_point.grid(row=6, column=1)



# Add parentheses buttons
button_open_paren = tk.Button(window, text="(", command=lambda: add_to_field("("), width=5, font=("Times New Roman", 14))
button_open_paren.grid(row=6, column=2)

button_close_paren = tk.Button(window, text=")", command=lambda: add_to_field(")"), width=5, font=("Times New Roman", 14))
button_close_paren.grid(row=6, column=3)



# Add the clear button
button_clear = tk.Button(window, text="C", command=clear, width=5, font=("Times New Roman", 14))
button_clear.grid(row=5, column=1)



# Remove button
button_clear = tk.Button(window, text="Remove", command=remove_last_character, width=5, font=("Times New Roman", 14))
button_clear.grid(row=7, column=2)



# Add the equal button
button_equals = tk.Button(window, text="=", command=calculate, width=5, font=("Times New Roman", 14))
button_equals.grid(row=5, column=3)



# Start the main loop
window.mainloop()
