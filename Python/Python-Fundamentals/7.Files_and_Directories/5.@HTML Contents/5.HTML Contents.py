def insert_after(haystack, needle, new_text):
    """Inserts 'new_text' into 'haystack' right after 'needle'."""
    # say:
    # haystack = '123'      i = 2
    # needle = '3'          needle_length = 1
    # new_text = '456'

    # https://stackoverflow.com/questions/20702124/find-a-string-and-insert-text-after-it-in-python
    i = haystack.find(needle)
    if i == -1:
        raise Exception('No substring found.')
    needle_length = len(needle)
    beginning = haystack[:i+needle_length]
    ending = haystack[i+needle_length:]
    return beginning + new_text + ending


def html_skeleton_creator():
    data = input()
    title = ''
    body = ''
    while data != 'exit':
        tag, content = data.split()
        element = f"\t<{tag}>{content}</{tag}>\n"
        if tag == 'title':
            title = element
        else:
            body += element
        data = input()
    html5 = f"""<!DOCTYPE html>
<html>
<head>
    {title.strip()}        
</head>
<body>
    {body.strip()}
</body>
</html>
"""
    with open('index.html', 'w') as w_file:
        w_file.write(html5)


def html_skeleton_creator_reversed():
    data = input()
    html5 = f"""<!DOCTYPE html>
<html>
    <head>      
    </head>
    <body>
    </body>
</html>
"""
    title = ''
    while data != 'exit':
        tag, content = data.split()
        element = f"<{tag}>{content}</{tag}>"
        if tag == 'title':
            title = element
        else:
            html5 = insert_after(html5, '<body>', new_text=f'\n\t\t{element}')
        data = input()

    html5 = insert_after(html5, '<head>', new_text=f"\n\t\t{title}")
    with open('index.html', 'w') as w_file:
        w_file.write(html5)


if __name__ == '__main__':
    # print(insert_after("Hello World", "lo", " beautiful"))  # prints 'Hello beautiful World'
    # print(insert_after('123', '3', '456'))                  # prints 123456
    html_skeleton_creator()

# Example Input:
"""
h1 Heading
h2 Heading
h3 Heading
h4 Heading
h5 Heading
h6 Heading
title Test
p 1.Paragraph
p 2.ParagraphTwo
div SimpleDiv
title HTML-Contents
exit
"""
