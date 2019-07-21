from tkinter import messagebox, END, Label, Button, Tk, Text, NSEW, Grid, TclError
import twitter
import tweepy
from Web_Scraping.program_functions.config import ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Twitter API part
# Program Authentication
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_KEY,
                  access_token_secret=ACCESS_SECRET)


def print_user_info(text_entry, output, window):
    username = text_entry.get()                            # Get/Fetch the user
    if username and username != 'Search for a user here':
        try:
            user = api.GetUser(screen_name=username)       # Get the user object
            output.delete(1.0, END)                        # Clear the text box from any previous info
            # _________________________________________________________________________________________________________
            # Insert information about the user:
            output.insert(END, f"Information for: {user.name} with a username @{user.screen_name}\n")
            try:
                output.insert(END, f"Location: {user.location}\n" if user.location else f"Location: Not provided.\n")
            except TclError:
                pass
            try:
                output.insert(END, f"Description: {user.description}\n" if user.description
                                   else f"Description: Not provided.\n")
            except TclError:
                pass

            output.insert(END, f"Website: {user.url}\n" if user.url else f"Website: Not provided.\n")
            output.insert(END, f"Followers: {user.followers_count}\n")
            output.insert(END, f"Friends: {user.friends_count}\n")
            output.insert(END, f"Total Tweets: {user.statuses_count}\n")
            profile_pic = get_profile_image(user.profile_image_url_https)
            panel = Label(window, image=profile_pic)
            panel.image = profile_pic
            panel.grid(row=1, column=0)
            # _________________________________________________________________________________________________________

            activity_button = Button(window, text='Show user recent activity', command=lambda: show_recent_activity(user),
                                     activeforeground='red', activebackground='yellow', bg='orange',
                                     relief="solid", cursor="hand2", width=20)
            activity_button.grid(row=2, column=0)
        except twitter.error.TwitterError:
            messagebox.showwarning("Warning", "No user exists with such a @username.")
    else:
        messagebox.showwarning("Warning", "You need to enter a username.")


def get_profile_image(url):
    # Credits: https://python-forum.io/Thread-Display-image-from-URL
    """
    Function to get the profile picture of the searched user.
    """
    response = requests.get(url.replace("_normal", ""))
    img_data = Image.open(BytesIO(response.content))
    img = img_data.resize((250, 250))
    profile_picture = ImageTk.PhotoImage(img)
    return profile_picture


def show_recent_activity(user):
    """
    The function creates a new tkinter window and a new Twitter API object in order to show a user recent activity on
    Twitter.
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api2 = tweepy.API(auth)                          # Authenticate the new Twitter API object
    username = user.screen_name
    tweets = api2.user_timeline(screen_name=username, count=5)
    if not tweets:
        messagebox.showwarning("Warning", "No recent activity.")
        return
    window = Tk()                                    # Create window
    window.title('User recent activity')             # Set title
    window.configure(bg='black')                     # change background color
    Grid.rowconfigure(window, 0, weight=0)           # Making the window resizeable
    Grid.columnconfigure(window, 0, weight=1)        # Making the window resizeable

    text_box = Text(window, bg="grey", fg="black", cursor='arrow', height=35,
                    highlightthickness=2, highlightbackground='orange')
    text_box.grid(row=0, column=0, sticky=NSEW)

    for status in tweets:                                       # Show the last statuses
        try:
            text_box.insert(END, f"On: {status.created_at}: User Tweeted:\n{status.text}\n\n")
        except TclError:
            pass
    window.mainloop()
