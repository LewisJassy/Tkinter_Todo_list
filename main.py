import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Todo List")
window.minsize(400, 400)


def add_button():
    enter = add_task.get()
    with open("todo.txt", "a") as data:
        data.write(f"{enter}\n")
        add_task.delete(0, tkinter.END)


def view_button():
    with open("todo.txt", "r") as text:
        file = text.readlines()
        formatted_content = "\n".join([f"{i + 1}. {line.strip()}" for i, line in enumerate(file)])
        messagebox.showinfo("Todo Content", formatted_content)


def delete_task():
    with open("todo.txt", "r") as text:
        file = text.readlines()
    num = int(delete_list.get())
    if 1 <= num <= len(file):
        del file[num - 1]
        delete_list.delete(0, tkinter.END)
        with open("todo.txt", "w") as text:
            text.writelines(file)


def exit_program():
    window.quit()


header = Label(text="TODO LIST", font=("Courier", 20, "bold"))
header.grid(column=1)
add = Button(text="Add", font=("Courier", 10, "bold"), command=add_button)
add.grid(column=0, row=1)
add_task = Entry(width=35)
add_task.grid(column=1, row=1)
view = Button(text="View", font=("Courier", 10, "bold"), command=view_button)
view.grid(column=1, row=3)
remove_task = Button(text="Delete", font=("courier", 10, "bold"), command=delete_task)
remove_task.grid(column=0, row=4)
delete_list = Entry(width=10)
delete_list.grid(column=1, row=4)
exit_button = Button(text="EXIT", font=("courier", 10, "bold"), command=exit_program)
exit_button.grid(column=1, row=6)

window.mainloop()
