# Tkinter GUI part
from tkinter import *
from Web_Scraping.program_functions.functions import print_user_info


# Мain:
window = Tk()                                    # create window
window.title('Twitter Accounts Reviewer')        # set title
window.configure(bg='black')                     # change background color


# Making the window resizeable and creating an upper frame
# https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
upper_frame = Frame(window, bg='black')
upper_frame.grid(row=0, column=0)
Grid.rowconfigure(window, 0, weight=0)
Grid.columnconfigure(window, 0, weight=1)  # https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter


# Text entry box for searching a user
text_entry = Entry(upper_frame, width=40, insertbackground='red', relief="solid", justify='center', highlightthickness=2)
text_entry.grid(row=0, column=0)
text_entry.insert(0, 'Search for a user here')
text_entry.bind("<Button-1>", lambda event: text_entry.delete(0, END))              		 # placeholder


# 'Search' button
search_button = Button(upper_frame, text='Search', activeforeground='red', activebackground='yellow', bg='green',
                       relief="solid", cursor="hand2", width=10,
                       command=lambda: print_user_info(text_entry, text_box, window))
search_button.grid(row=0, column=1)
window.bind("<Return>", (lambda event: print_user_info(text_entry, text_box, window)))   # On enter-press binding

# Text Box for displaying the user information
text_box = Text(window, bg="grey", fg="black", cursor='arrow', height=35,
                highlightthickness=2, highlightbackground='orange')
text_box.grid(row=1, column=0, sticky=NSEW)


# Run the main loop
window.mainloop()
