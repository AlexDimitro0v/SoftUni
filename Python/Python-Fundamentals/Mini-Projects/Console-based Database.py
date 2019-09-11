# A simple implementation of a basic people database
import pickle
# The pickle module is used for saving
# Credits: https://stackoverflow.com/questions/27745500/how-to-save-a-list-to-a-file-and-read-it-as-a-list-type

"""
Note: Instead of using flying functions, a class 'Database' could be created, which turns all the database functions 
into methods and encapsulates the information.
"""
database = []  # global variable to be used to store the database


class Person:
    def __init__(self, name, phone_number, town):
        self.name = name
        self.phone_number = phone_number
        self.town = town


def pick_option(option):
    # Credits: https://jaxenter.com/implement-switch-case-statement-python-138315.html?
    menu = {
        '1': search_by_name,
        '2': search_by_town,
        '3': search_by_tel_number,
        '4': display_database,
        '5': add_person,
        '6': delete_person,
        'M': display_menu,
        'Q': terminate
    }
    try:
        func = menu[option]
        func()
    except KeyError:
        print('Invalid command. Please enter a value between 1 and 6.')
    # func = menu.get(option, lambda: 'Invalid command. Please enter a value between 1 and 6.')


def display_menu():
    """This function informs the user about the available operations and forces the user to pick one."""
    print("====================================================================================================")
    print("Press 1 to search people by name.")
    print("Press 2 to search people by town.")
    print("Press 3 to search people by tel.number.")
    print("Press 4 to display all the people in the database.")
    print("Press 5 to add a new person.")
    print("Press 6 to delete a person.")
    print("Choose your move: ", end='')
    choice = input().upper()
    while choice not in map(str, [1, 2, 3, 4, 5, 6]):
        print('Invalid command. Please enter a value between 1 and 6.')
        choice = input().upper()
    print("====================================================================================================")
    pick_option(choice)


def search_by_name():
    print('-'*50)
    print('You have chosen to search by name.')
    name = input("Name of the person: ")
    filtered_names_list = list(filter(lambda p: p.name == name, database))
    if filtered_names_list:
        display_people(filtered_names_list)
    else:
        print(f"No records found for '{name}'.")
        # print("No records found for this name.\n")
    print('-'*50+'\n\n')


def search_by_town():
    print('-'*50)
    print('You have chosen to search by town.')
    town = input("Enter a town: ")
    filtered_towns_list = list(filter(lambda p: p.town == town, database))
    if filtered_towns_list:
        display_people(filtered_towns_list)
    else:
        print(f"No records found for '{town}'.")
        # print("No records found for this town.\n")
    print('-'*50+'\n\n')


def search_by_tel_number():
    print('-'*50)
    print('You have chosen to search by phone number.')
    phone_number = input("Enter the telephone number: ")
    filtered_phones_list = list(filter(lambda p: p.phone_number == int(phone_number), database))
    if filtered_phones_list:
        display_people(filtered_phones_list)
    else:
        print(f"No records found for '{phone_number}'.")
        # print("No records found for this telephone number.\n")
    print('-'*50+'\n\n')


def display_database():
    print('-'*50)
    display_people(database)
    print('-'*50+'\n\n')


def add_person():
    print('-'*50)
    print('You have chosen to add a new person to the database.')

    while True:
        name = input("Name of the person: ")
        if 2 > len(name) < 255 or not name.isalpha():
            print("Invalid name. Try again.")
            continue
        break

    # -----------------------------------------------------------------------------------------------------------
    # Valid tel.number check
    tel_numbers_list = [p.phone_number for p in database]
    while True:
        try:
            tel_number = int(input("Person's phone number: "))
            # if the number is not unique continue looping, else break the while loop
            if tel_number in tel_numbers_list:
                print("This telephone number has already been registered. Try again with another one.")
                continue
            elif 3 > len(str(tel_number)) < 15:
                print("Invalid phone number. Try again.")
                continue
            break
        except ValueError:
            print("Invalid phone number. Try again.")
    # -----------------------------------------------------------------------------------------------------------

    while True:
        town = input("Person's town: ")
        if 2 > len(town) < 255 or not town.isalpha():
            print("Invalid town. Try again.")
            continue
        break

    new_person = Person(name, tel_number, town)
    database.append(new_person)
    print("Person added successfully.")
    print('-'*50+'\n\n')


def delete_person():
    print('-'*50)
    print('You have chosen to delete a person.')
    name = input("Name of the person: ")
    filtered_names_list = list(filter(lambda p: p.name == name, database))
    if filtered_names_list:     # if there are values inside
        if len(filtered_names_list) > 1:
            print(f"There are several people called '{name}'", end='\n-')
            town = input("Give a town to specify who you want to delete: ")
            filtered_towns_list = list(filter(lambda p: p.town == town, filtered_names_list))
            if filtered_towns_list:
                if len(filtered_towns_list) > 1:
                    print(f"There are several people called '{name}' in town: '{town}'", end='\n-')
                    phone_number = input("Give a tel.number to specify who you want to delete: ")
                    filtered_phones_list = list(filter(lambda p: p.phone_number == int(phone_number), filtered_towns_list))
                    if filtered_phones_list:                    # we found the person we want to delete
                        database.remove(*filtered_phones_list)  # delete the person by unpacking the list storing him
                        pass
                    else:
                        print(f"No records found for '{name}' in town: '{town}' with tel.number: '{phone_number}'.")
                        print('-' * 50 + '\n\n')
                        return
                else:                                      # we found the person we want to delete
                    database.remove(*filtered_towns_list)  # delete the person by unpacking the list storing him
                    pass
            else:
                print(f"No records found for '{name}' in town: '{town}'.")
                print('-' * 50 + '\n\n')
                return
        else:                                             # we found the person we want to delete
            database.remove(*filtered_names_list)         # delete the person by unpacking the list storing him
            pass
    else:
        print(f"No records found for '{name}'.")
        print('-' * 50 + '\n\n')
        return

    print("Person deleted successfully.")
    print('-'*50+'\n\n')


def terminate():
    exit()


def load():
    global database     # so we can work with the global variable
    try:                # try loading the database
        with open('save.pickle', 'rb') as load_file:
            database = pickle.load(load_file)
    except FileNotFoundError:
        pass


def display_people(lst):
    print(f"Number of records found: {len(lst)}\n")
    for person in lst:
        print(f"Name: {person.name}")
        print(f"Phone number: {person.phone_number}")
        print(f"Town: {person.town}\n")


def save():
    with open("save.pickle", "wb") as save_file:
        pickle.dump(database, save_file)


def main():
    load()
    while True:
        print("Press 'M' to see the available operations.")
        print("Press 'Q' to quit the program.\n")
        choice = input().upper()
        pick_option(choice)
        save()


if __name__ == '__main__':
    main()
