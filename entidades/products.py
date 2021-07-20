class Products:
    def __init__(self, product_id, product_name, department_id):
        self.__product_id = product_id
        self.__product_name = product_id
        self.__department_id = department_id       

    def set_product_id(self, product_id):
        self.__product_id = product_id      

    def set_product_name(self, product_name):
        self.__product_id = product_id            

    def set_department_id(self, department_id):
        self.__department_id = department_id

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_department_id(self):
        return self.__department_id
