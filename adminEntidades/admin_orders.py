class Admin_Orders:

    def __init__(self, db):
        self.__cnx = db

    def create(self, order_id, user_id, order_number, order_dow, days_since_prior_order):
        cursor = self.__cnx.cursor()
        insert = f"insert into orders(order_id, user_id, order_number, order_dow, days_since_prior_order) values ('{order_id}', ('{user_id}', ('{order_number}', ('{order_dow}', ('{days_since_prior_order}')"
        cursor.execute(insert)
        self.__cnx.commit()
        cursor.close()

    def update(self, order_id, user_id, order_number, order_dow, days_since_prior_order):
        cursor = self.__cnx.cursor()
        idi = self.select(order_id)
        update = f'update orders set order_number = "{orders.get_order_number()}", order_dow = "{orders.get_order_dow()}, days_since_prior_order = "{orders.get_days_since_prior_order()} where id = {idi}'
        cursor.execute(update)
        self.__cnx.commit()
        cursor.close()

    def select(self, order):
        cursor = self.__cnx.cursor()
        select = f"Select id from orders where order_number = '{order_number}'"
        cursor.execute(select)
        res = cursor.fetchall()
        cursor.close()
        return res[0][0]

    def get_order(self, order_number):
        cursor = self.__cnx.cursor()
        query = f"Select * from orders where order_number = '{order_number}'"
        cursor.execute(select)
        res = cursor.fetchall()
        user_id = res[0][0]
        order = res[0][1]
        cursor.close()
        return res[0]

    def get_all(self):
        cursor = self.__cnx.cursor()
        select = f"Select * from orders"
        cursor.execute(select)
        res = cursor.fetchall()
        cursor.close()
        return res