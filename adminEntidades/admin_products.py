from adminEntidades.admin_departments import Admin_Departments
class Admin_Products:

    def __init__(self, db):
        self.__cnx = db

    def create(self, product_id, product_name, department_id):
        cursor = self.__cnx.cursor()
        insert = f"insert into products(product_id, product_name, department_id) values ('{product_id}','{product_name}','{department_id}')"
        cursor.execute(insert)
        self.__cnx.commit()
        cursor.close()

    def update(self, product_id, product_name):
        cursor = self.__cnx.cursor()
        id = self.select(viejo)
        update = f'update products set product_id = "{product.product_id)}", product_name = "{product.get_product_namea()}" where id = {idi}'
        cursor.execute(update)
        self.__cnx.commit()
        cursor.close()

    def select(self, product_name):
        cursor = self.__cnx.cursor()
        select = f"Select id from products where product_name = '{product_name}'"
        cursor.execute(select)
        res = cursor.fetchall()
        cursor.close()
        return res[0][0]

    def get_product(self, product_name):
        cursor = self.__cnx.cursor()
        query = f"Select * from products where product_name = '{product_name}'"
        cursor.execute(select)
        res = cursor.fetchall()
        product_id = res[0][0]
        product_name = res[0][1]
        cursor.close()
        return Products(product_id, product_name)

    def get_all(self):
        cursor = self.__cnx.cursor()
        select = f"Select * from products"
        cursor.execute(select)
        res = cursor.fetchall()
        cursor.close()
        return res