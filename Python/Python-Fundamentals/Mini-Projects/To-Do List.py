from tkinter import *
# Good Practice:
# The grid method should be separated from the initialization, because the grid method returns None.
to_do_list = []


def save():
    with open('save_file.txt', 'a') as f:
        for item in to_do_list:
            f.write(f"{item}\n")


def add():
    task = text_entry.get()        # Get the task 
    if task:
        to_do_list.append(task)
        text_entry.delete(0, END)  # Clear the text entry box
        output.insert(END, task)   # Insert the task into the To-Do Listbox


def close():
    save()
    exit()

# ______________________________________________________________________________________________________________________
# Tkinter GUI part


# Мain:
window = Tk()
window.title('To-DO List: ')
window.geometry('500x250')


# Create a text entry box for adding a task
Label(window, text="Task:").grid(row=0, column=0, sticky=N)
text_entry = Entry(window, fg='white', bg='black', width=25, insertbackground='white')
text_entry.grid(row=0, column=1, sticky=N)


# 'Add' button
add_button = Button(window, text='Add', cursor="plus", activeforeground='white', activebackground='black', bg='yellow',
                    relief="solid", command=add)
add_button.grid(row=1, padx=10, pady=20)


# 'Quit' button
add_button = Button(window, text='Quit', cursor="X_cursor", activeforeground='white', activebackground='black',
                    bg='red', relief="solid", command=close)
add_button.grid(row=1, column=10, padx=20, pady=20)


# Create a text box
output = Listbox(window, height=10, width=25, fg='black', relief="solid")
output.grid(row=0, column=3, padx=15)


# Run the main loop
window.mainloop()
