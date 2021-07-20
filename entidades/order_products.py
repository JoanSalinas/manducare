class Order_Products:
    def __init__(self, order_id, product_id, reordered):
        self.__order_id = order_id
        self.__product_id = product_id
        self.__reordered = reordered       

    def set_order_id(self, order_id):
        self.__order_id = order_id      

    def set_product_id(self, product_id):
        self.__product_id = product_id            

    def set_reordered(self, reordered):
        self.__reordered = reordered

    def get_order_id(self):
        return self.__order_id

    def get_product_id(self):
        return self.__product_id

    def get_reordered(self):
        return self.__reordered
