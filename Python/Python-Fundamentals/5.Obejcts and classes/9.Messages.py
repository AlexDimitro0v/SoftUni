import itertools as it


class User:
    def __init__(self, username, received_messages=[]):
        self.username = username
        self.received_messages = received_messages

    def add_received_messages(self, message):
        if not self.received_messages:
            self.received_messages = []
            # a new empty list because else it shares the same list from the default with the other Users
        self.received_messages += [message]

    def __str__(self):
        return self.username


class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


def main():
    data = input()
    usernames_list = []          # registered users
    while data != 'exit':
        registered_usernames = [obj.username for obj in usernames_list]
        data = data.split()
        if data[0] == 'register':
            username = data[1]
            user = User(username)
            if username not in registered_usernames:
                usernames_list.append(user)
        else:
            sender = data[0]
            recipient = data[2]
            content = data[3:]     # returns a list
            if sender in registered_usernames and recipient in registered_usernames:
                for obj in usernames_list:
                    if obj.username == recipient:
                        User.add_received_messages(obj, Message(*content, sender))
        data = input()

    user_sender, user_recipient = input().split()

    filtered_usernames = list(filter(lambda x: x.username == user_sender or x.username == user_recipient,
                                     usernames_list))

    recipient_received_msgs = [msg.content
                               for obj in filtered_usernames
                               if obj.username == user_recipient
                               for msg in obj.received_messages
                               if msg.sender == user_sender
                               ]
    sender_received_msgs = [msg.content
                            for obj in filtered_usernames
                            if obj.username == user_sender
                            for msg in obj.received_messages
                            if msg.sender == user_recipient
                            ]

    conversation = list(it.zip_longest(recipient_received_msgs, sender_received_msgs))
    if not conversation:
        print("No messages")
        return

    for pair in conversation:
        if pair[0]:
            print(f"{user_sender}: {pair[0]}")
        if pair[1]:
            print(f"{pair[1]} :{user_recipient}")


if __name__ == '__main__':
    main()
