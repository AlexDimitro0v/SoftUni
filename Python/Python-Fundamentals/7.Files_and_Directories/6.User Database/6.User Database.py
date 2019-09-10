import pickle
users = {}


def load():
    global users
    try:                # try loading the database
        with open('save.pickle', 'rb') as load_file:
            users = pickle.load(load_file)
    except FileNotFoundError:
        users = {}


def save():
    with open("save.pickle", "wb") as save_file:
        pickle.dump(users, save_file)


def control_menu():
    data = input()
    logged_in = False
    while data != 'exit':
        command = data.split()[0]
        if command == 'register':
            _, username, password, pass_confirmation = data.split()
            # username, password, pass_confirmation = data.split()[1:]  alternative
            if username in users:
                print("The given username already exists.")
            elif password != pass_confirmation:
                print("The two passwords must match.")
            else:
                users[username] = password

        elif command == 'login':
            username, password = data.split()[1:]
            if username not in users:
                print("There is no user with the given username.")
            elif username in users and password != users[username]:
                print("The password you entered is incorrect.")
            elif logged_in:
                print("There is already a logged in user.")
            else:
                logged_in = True

        elif command == 'logout':
            if logged_in:
                logged_in = False
            else:
                print("There is no currently logged in user.")
        data = input()


if __name__ == '__main__':
    load()
    control_menu()
    save()


"""
register Simo 123 123
register Ivo 123 132
login Simo 132
login Simo 123
logout
register pesho pesho pesho
login Ivo 123
login pesho pesho
exit

register Merry 123456 123456
register pesho pesho pesho
logout
login Simo 123
logout
exit
"""
