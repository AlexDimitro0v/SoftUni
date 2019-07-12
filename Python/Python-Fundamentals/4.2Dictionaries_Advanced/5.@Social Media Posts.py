# Dictionaries inside a Dictionary
def create_main_dic():
    posts = dict()
    data = input()
    while data != "drop the media":
        data = data.split(' ')
        command = data[0]
        post_name = data[1]
        if command == "post":
            posts[post_name] = {'Likes': 0, 'Dislikes': 0, 'Comments': {}}

        elif command == "like":
            posts[post_name]['Likes'] += 1

        elif command == "dislike":
            posts[post_name]['Dislikes'] += 1

        elif command == "comment":
            commentator_name = data[2]
            commentator_comment = data[3:]
            posts[post_name]['Comments'].update({commentator_name: commentator_comment})

        data = input()

    return posts


def drop_the_media(posts):
    for key, value in posts.items():
        print(f'Post: {key} ', end='')
        for inner_key, inner_value in value.items():
            if inner_key != "Comments":
                print(f'| {inner_key}: {inner_value}', end=' ')
            else:
                print(f'\n{inner_key}:')
                if inner_value:
                    for key3, value3 in inner_value.items():
                        print(f"*  {key3}: {' '.join(value3)}")
                else:
                    print("None")


def main():
    dic = create_main_dic()
    drop_the_media(dic)


if __name__ == '__main__':
    main()
