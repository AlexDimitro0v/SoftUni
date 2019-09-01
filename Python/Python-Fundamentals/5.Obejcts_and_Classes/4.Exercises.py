# https://codereview.stackexchange.com/questions/126100/recording-all-instances-of-a-class-python
# https://stackoverflow.com/questions/12101958/how-to-keep-track-of-class-instances
# Recording all instances of a class
list_exercises = []


class Exercise:
    def __init__(self, topic, course_name, link, problems):
        # setting the properties of our objects
        self.topic = topic
        self.course_name = course_name
        self.link = link
        self.problems = problems                # a list
        list_exercises.append(self)

    def print_info(self):
        print(f"Exercises: {self.topic}")
        print(f"Problems for exercises and homework for the \"{self.course_name}\" course @ SoftUni.")
        print(f"Check your solutions here: {self.link}")

        for index, item in enumerate(self.problems):
            print(f"{index+1}. {item}")


def create_object(data):
    topic, course_name, link, problems = data
    Exercise(topic, course_name, link, problems.split(', '))


def main():
    data = input()
    while data != "go go go":
        create_object(data.split(' -> '))
        data = input()

    for exercise in list_exercises:
        exercise.print_info()


if __name__ == '__main__':
    main()
