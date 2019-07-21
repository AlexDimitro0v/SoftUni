import pickle
from tkinter import END, messagebox
import sys
to_do_list = []                    # Global to-do list to store all the tasks


def update_task_list(output):
    # TODO: Optimize the process for a better performance
    output.delete(0, END)          # Clear the list
    for task in to_do_list:
        output.insert(END, task)   # Insert each task into the To-Do Listbox


def add_task(text_entry, output):
    task = text_entry.get()        # Get/Fetch the task
    if task and task != 'Add your task here':
        print(task)
        to_do_list.append(task)
        text_entry.delete(0, END)  # Clear the text entry box
        update_task_list(output)   # Update the To-Do Listbox
    else:
        messagebox.showwarning("Warning", "You need to enter a task.")


def clear_task_list(output):
    output.delete(0, END)
    to_do_list.clear()


def delete_selected_task(output):
    task = output.get("active")     # Get/Fetch the selected task
    if task in to_do_list:          # Check if task exist
        to_do_list.remove(task)     # Remove it from the to-do list
        update_task_list(output)    # Update the To-Do Listbox


def load():
    global to_do_list
    try:
        family_file = open("save.pickle", "rb")
        to_do_list = pickle.load(family_file)
    except FileNotFoundError:
        to_do_list = []


def save():
    with open("save.pickle", "wb") as save_file:
        pickle.dump(to_do_list, save_file)


def close():
    question = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
    if question == 'yes':
        save()
        sys.exit(0)
