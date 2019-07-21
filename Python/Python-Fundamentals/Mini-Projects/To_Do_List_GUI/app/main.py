from tkinter import *
from To_Do_List_GUI.program_functions import functions     # importing the interactive command functions

# ______________________________________________________________________________________________________________________
# Tkinter GUI part - using pack() as a main geometry manager

# How to place grid elements next to each other:
# https://stackoverflow.com/questions/43148463/how-to-place-widgets-next-to-each-other/43148616

# Мain:
functions.load()                    # try loading previous tasks
window = Tk()                       # create window
window.title('To-DO List: ')        # set title
window.configure(bg='black')        # change background color
print("Daily Tasks:")


# Add Frames
bottom_frame = Frame(window, bg='black')
bottom_frame.pack(side="bottom", fill="both", expand=False)           # container for the bottom widgets
right_frame = Frame(window, bg='black')
right_frame.pack(side="right", fill="both", expand=True, pady=30)     # container for the right widgets


# Create a label for the To-Do List
label = Label(text='To-Do List:', bg='black', fg='white')
label.pack(side='top')

# Create a listbox for displaying the to-do list
output = Listbox(window, height=8, width=30, fg='black', bg='grey', relief="solid")
output.pack(side="left", fill="both", expand=True)

# 'Add' button
add_button = Button(right_frame, text='Add', activeforeground='red', activebackground='yellow', bg='green',
                    relief="solid", command=lambda: functions.add_task(text_entry, output), cursor="plus", width=5)
add_button.grid(row=0, column=1, sticky=W, padx=4)


# Text entry box for adding a task
text_entry = Entry(right_frame, bg='grey', width=25, insertbackground='red', relief="solid")
text_entry.grid(row=1, column=1, padx=5)
text_entry.insert(0, 'Add your task here')
text_entry.bind("<Button-1>", lambda event: text_entry.delete(0, END)) # placeholder


# More buttons
# Note lambda: https://stackoverflow.com/questions/15589351/tkinter-command-to-call-function-from-another-python-script
buttons = {'Delete Task': lambda: functions.delete_selected_task(output),
           'Clear List': lambda: functions.clear_task_list(output),
           'Quit': functions.close
           }
c = 0
for key, f in buttons.items():
    Button(bottom_frame, text=key, relief='solid', width=15, height=1, bg='red', command=f, cursor="X_cursor",
           activeforeground='red', activebackground='white')\
        .grid(row=1, column=c, pady=10)
    c += 1


# Run the main loop
def main():
    functions.load()        # try loading any previous tasks
    window.mainloop()
    functions.save()        # save before leaving


if __name__ == '__main__':
    main()
