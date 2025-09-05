from employee import Employee

class Worker(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked  # Private attribute

    def display_info(self):
        super().display_info()
        print("Hours Worked:", self.__hours_worked)

    # Getter and Setter methods for hours_worked
    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked
