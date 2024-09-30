
# For graphical interface
import tkinter as tk

#Field text for the show of number and operation
field_text = "1"
def add_to_field(sth):
    global field_text
    field_text = field_text+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",field_text)

#Calculate function for the result
def calculate():
    global field_text
    result = str(eval(field_text))
    field.delete("1.0","end")
    field.insert("1.0",result)


window = tk.Tk()
window.geometry("300x300")
field = tk.Text(window,height=2,width=21,font=("Times New Roman", 20))
field.grid(row = 1, column = 1, columnspan = 4)
window.mainloop()