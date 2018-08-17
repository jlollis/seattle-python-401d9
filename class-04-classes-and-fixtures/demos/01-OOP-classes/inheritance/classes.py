class Human:
    height = 0


class Person(Human):
    def __init__(self, name, age, children=None):
        self.first_name = name
        self.years_old = age
        self.children = children

        if not self.children:
            self.children = []

        for child in self.children:
            # do something with child
            pass


class Employee(Person):
    def __init__(self, emp_id, name, age, children=None, car=None):
        if type(emp_id) is not int:
            raise TypeError('Employee ID must be valid integer')

        self.emp_id = emp_id
        # self.emp_id = emp_id if type(emp_id) is int else None
        super().__init__(name, age, children)

    def __repr__(self):
        return f'<Employee ID: {self.emp_id}, Name: {self.first_name}>'

    def __str__(self):
        return f'Name: {self.first_name}, ID: {self.emp_id}'

    def _private_method(self):
        pass

    def say_name(self):
        return f'Hello my name is {self.first_name}'

    @classmethod
    def hire_new_employee():
        #
        pass
