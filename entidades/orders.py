class Orders:
    def __init__(self, order_id, user_id, order_number, order_dow, days_since_prior_order):
        self.__order_id = order_id
        self.__user_id = user_id    
        self.__order_number = order_number            
        self.__order_dow = order_dow
        self.__days_since_prior_order = days_since_prior_order      

    def set_order_id(self, order_id):
        self.__order_id = order_id      

    def set_user_id(self, user_id):
        self.__user_id = user_id            

    def set_order_number(self, order_number):
        self.__order_number = order_number

    def set_order_dow(self, order_dow):
        self.__order_dow = order_dow

    def set_days_since_prior_order(self, days_since_prior_order):
        self.__days_since_prior_order = days_since_prior_order

    def get_order_id(self):
        return self.__order_id

    def get_user_id(self):
        return self.__user_id

    def get_order_number(self):
        return self.__order_number

    def get_order_dow(self):
        return self.__order_dow
    
    def get_days_since_prior_order(self):
        return self.__days_since_prior_order