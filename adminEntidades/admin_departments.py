class Admin_Departments:

    def __init__(self, db):
        self.__cnx = db

    def update(self, department):
        cursor = self.__cnx.cursor()
        idi = self.select(department.get_department_id())
        update = f"update departments set department = '{department.get_department()}' where id = {idi}"    
        cursor.execute(update)
        self.__cnx.commit()
        cursor.close()

    def get_department(self, department):
        cursor = self.__cnx.cursor()
        query = f"Select * from departments where department = '{department}'"
        cursor.execute(select)
        res = cursor.fetchall()
        department_id = res[0][0]
        department = res[0][1]
        cursor.close()
        return Departments(department_id, department)

    def get_all(self):
        cursor = self.__cnx.cursor()
        select = f"Select * from departments"
        cursor.execute(select)
        res = cursor.fetchall()
        cursor.close()
        return res