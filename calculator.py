import tkinter as tk

# Field text for the display of numbers and operations
field_text = "1"

def add_to_field(sth):
    global field_text
    field_text = field_text + str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

# Calculate function for the result
def calculate():
    global field_text
    result = str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)

# Function that will clear the field
def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")

# Create the main window
window = tk.Tk()
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

# Start the main loop
window.mainloop()
