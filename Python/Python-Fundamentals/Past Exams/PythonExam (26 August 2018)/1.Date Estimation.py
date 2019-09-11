from datetime import datetime


def main():
    current_date = datetime(2018, 8, 26)
    year, month, date = input().split('-')
    exam_date = datetime(int(year), int(month), int(date))

    if current_date == exam_date:
        print("Today date")
    elif current_date > exam_date:
        print("Passed")
    else:
        print(f"{(exam_date - current_date).days + 1} days left")


if __name__ == '__main__':
    main()
