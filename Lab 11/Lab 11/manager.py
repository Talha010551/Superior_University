from employee import Employee

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department  # Private attribute

    def display_info(self):
        super().display_info()
        print("Department:", self.__department)

    # Getter and Setter methods for department
    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department
