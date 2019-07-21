from tkinter import END, messagebox, Label
import twitter
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
            # Insert information about the user:
            output.insert(END, f"Information for: {user.name} with a username @{user.screen_name}\n")
            output.insert(END, f"Location: {user.location}\n" if user.location else f"Location: Not provided.\n")
            output.insert(END, f"Description: {user.description}\n" if user.description
                               else f"Description: Not provided.\n")
            output.insert(END, f"Website: {user.url}\n" if user.url else f"Website: Not provided.\n")
            output.insert(END, f"Followers: {user.followers_count}\n")
            output.insert(END, f"Friends: {user.friends_count}\n")
            output.insert(END, f"Total Tweets: {user.statuses_count}\n")

            profile_pic = get_profile_image(user.profile_image_url_https)
            panel = Label(window, image=profile_pic)
            panel.image = profile_pic
            panel.grid(row=1, column=0)
            #
            # output.insert(END, "--------------------------------Recent Activity:-------------------------------\n")
            # # username = user.screen_name
            # # last_tweets = tweets(username)
            # # for status in last_tweets:
            #    #  output.insert(END, status)
        except twitter.error.TwitterError:
            messagebox.showwarning("Warning", "No user exists with such a @username.")
    else:
        messagebox.showwarning("Warning", "You need to enter a username.")


def tweets(name, batch_size=5):
    # Credits: https://gist.github.com/codeinthehole/0e7430d79f3dcd1235c89f9367a49a1b
    """
    Return a generator that emits tweet status information.
    """
    while True:
        # Fetch tweets in batches
        statuses = api.GetUserTimeline(screen_name=name, count=batch_size)
        if len(statuses) == 0:
            break
        for status in statuses:
            yield f"On: {status.created_at}: User Tweeted:\n{status.text}\n\n"


def get_profile_image(url):
    # Credits: https://python-forum.io/Thread-Display-image-from-URL
    """
    Function to get the profile pciture of the searched user.
    """
    response = requests.get(url.replace("_normal", ""))
    img_data = Image.open(BytesIO(response.content))
    img = img_data.resize((200, 200))
    profile_picture = ImageTk.PhotoImage(img)
    return profile_picture
