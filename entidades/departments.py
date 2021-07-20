class Departments:
    def __init__(self, department_id, department):
        self.__department_id = department_id
        self.__department = department

    def set_department_id(self, department_id):
        self.__department_id = department_id

    def set_department(self, department):
        self.__department = department

    def get_department_id(self):
        return self.__department_id

    def get_department(self):
        return self.__department
