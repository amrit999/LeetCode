class Address:
    def __init__(self,street_name,street_no):
        self.street_name = street_name
        self.street_no = street_no

class User(Address):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.address = ''

    def update_fn(self,first_name):
        self.first_name = first_name

    def update_ln(self,last_name):
        self.last_name = last_name

    def add_addrees(self,street_name,street_no):
        self.address = street_no + ' ' + street_name

    def ret_add(self):
        return self.address

    def ret_fn(self):
        return self.first_name

    def ret_ln(self):
        return self.last_name

    def ret_fullname(self):
        return self.first_name + ' ' + self.last_name


user = User('amrit','kaur')
print(user.ret_fn())
print(user.ret_ln())
print(user.ret_fullname())
user.update_fn('sushant')
user.update_ln('ahuja')
user.add_addrees('atwater','2021')
print(user.ret_fn())
print(user.ret_ln())
print(user.ret_fullname())
print(user.ret_add())



