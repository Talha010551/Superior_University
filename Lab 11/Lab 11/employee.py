class Employee:
    def __init__(self, name, age, salary):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute
        self.__salary = salary  # Private attribute

    def display_info(self):
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Salary:", self.__salary)

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_salary(self, salary):
        self.__salary = salary
