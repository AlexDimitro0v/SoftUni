from itertools import zip_longest


class User:
    def __init__(self, username):
        self.username = username
        self.received_messages = []


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

            # Skip if someone does not exist
            if sender in registered_usernames and recipient in registered_usernames:
                for obj in usernames_list:
                    if obj.username == recipient:
                        # Create a new message
                        obj.received_messages.append(Message(*content, sender))
        data = input()

    # Read users for report
    user_sender, user_recipient = input().split()

    recipient_received_msgs = [msg.content
                               for obj in filter(lambda x: x.username == user_recipient, usernames_list)
                               for msg in obj.received_messages
                               if msg.sender == user_sender
                               ]
    sender_received_msgs = [msg.content
                            for obj in filter(lambda x: x.username == user_sender, usernames_list)
                            for msg in obj.received_messages
                            if msg.sender == user_recipient
                            ]

    conversation = list(zip_longest(recipient_received_msgs, sender_received_msgs))
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
