class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def update_fn(self,new_first_name):
        self.first_name = new_first_name

    def update_ln(self,new_last_name):
        self.last_name = new_last_name

    def ret_fn(self):
        return self.first_name

    def ret_ln(self):
        return self.last_name

    def ret_fullname(self):
        return self.first_name + ' ' + self.last_name




