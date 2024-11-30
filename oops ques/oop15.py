# Popup Menu based Arithmetic Operations using Tkinter:
# Creating a popup menu is similar to creating a regular menu.
# First, you create an instance of Popup menu using Menu( ),
# and then you can add items to it using
# menu.add_command( ). Finally, you bind a widget with an
# event to pop up the menu. Popup menu commands are
# used to perform actions to be displayed in a canvas which is
# created using canvas( ).
# The canvas widget is used to add the structured graphics to
# the python application. It is used to display text, images,
# graph and plots to the python application. The menu items
# use callback functions to instruct the canvas to perform
# actions.
# In code, a popup menu is displayed by clicking the right
# mouse button followed by binding it with the canvas using
# canvas.bind( ). Each item in the popup menu is selected to
# perform the corresponding arithmetic operations. The
# inputs are obtained in two textboxes and the output is
# displayed in one textbox.


import tkinter as tk

def add():
    try:
        result = float(num1_entry.get()) + float(num2_entry.get())
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid input")

def subtract():
    try:
        result = float(num1_entry.get()) - float(num2_entry.get())
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid input")

def multiply():
    try:
        result = float(num1_entry.get()) * float(num2_entry.get())
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid input")

def divide():
    try:
        num2 = float(num2_entry.get())
        if num2 == 0:
            raise ZeroDivisionError
        result = float(num1_entry.get()) / num2
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid input")
    except ZeroDivisionError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Cannot divide by zero")

def popup(event):
    popup_menu.post(event.x_root, event.y_root)

root = tk.Tk()
root.title("Arithmetic Operations")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

num1_label = tk.Label(canvas, text="Number 1:")
num1_label.place(x=50, y=20)

num2_label = tk.Label(canvas, text="Number 2:")
num2_label.place(x=50, y=50)

result_label = tk.Label(canvas, text="Result:")
result_label.place(x=50, y=80)

num1_entry = tk.Entry(canvas)
num1_entry.place(x=120, y=20)

num2_entry = tk.Entry(canvas)
num2_entry.place(x=120, y=50)

result_entry = tk.Entry(canvas)
result_entry.place(x=120, y=80)

popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="Add", command=add)
popup_menu.add_command(label="Subtract", command=subtract)
popup_menu.add_command(label="Multiply", command=multiply)
popup_menu.add_command(label="Divide", command=divide)

canvas.bind("<Button-3>", popup)

root.mainloop()
