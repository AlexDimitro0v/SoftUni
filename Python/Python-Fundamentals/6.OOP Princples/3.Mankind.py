from abc import ABC, abstractmethod


class Human(ABC):
    @abstractmethod
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    @property
    def f_name(self):
        return self._f_name

    @f_name.setter
    def f_name(self, f_name):
        if len(f_name) < 4:
            raise Exception("Expected length at least 4 symbols! Argument: firstName")
        elif not f_name[0].isupper():
            raise Exception("Expected upper case letter! Argument: firstName")
        self._f_name = f_name

    @property
    def l_name(self):
        return self._l_name

    @l_name.setter
    def l_name(self, l_name):
        if len(l_name) < 3:
            raise Exception("Expected length at least 3 symbols! Argument: lastName")
        elif not l_name[0].isupper():
            raise Exception("Expected upper case letter! Argument: lastName")
        self._l_name = l_name

    @abstractmethod
    def __str__(self):
        pass


class Student(Human):
    def __init__(self, f_name, l_name, id_number):
        super().__init__(f_name, l_name)
        self.id_number = id_number

    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        if not 5 <= len(id_number) <= 10 or not id_number.isalnum():
            raise Exception("Invalid faculty number!")
        self._id_number = id_number

    def __str__(self):
        return f"First Name: {self.f_name}\nLast Name: {self.l_name}\nFaculty number: {self.id_number}"


class Worker(Human):
    def __init__(self, f_name, l_name, weekly_salary, daily_work_hours):
        super().__init__(f_name, l_name)
        self.weekly_salary = float(weekly_salary)
        self.daily_work_hours = float(daily_work_hours)

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, weekly_salary):
        if weekly_salary < 10:
            raise Exception("Expected value mismatch! Argument: weekSalary")
        self._weekly_salary = weekly_salary

    @property
    def daily_work_hours(self):
        return self._daily_work_hours

    @daily_work_hours.setter
    def daily_work_hours(self, daily_work_hours):
        if not 1 <= daily_work_hours <= 12:
            raise Exception("Expected value mismatch! Argument: workHoursPerDay")
        self._daily_work_hours = daily_work_hours

    def calculate_hourly_wage(self, workdays=5):
        return self.weekly_salary/self.daily_work_hours/workdays

    def __str__(self):
        return f"First Name: {self.f_name}\nLast Name: {self.l_name}\nWeek Salary: {self.weekly_salary:.2f}\n" \
               f"Hours per day: {self.daily_work_hours:.2f}\nSalary per hour: {self.calculate_hourly_wage():.2f}"


def main():
    try:
        student = eval('Student')(*input().split())
        worker = eval('Worker')(*input().split())
        print(f"{student}\n")
        print(worker)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
