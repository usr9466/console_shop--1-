from classes.models.model import Model


'''
    simple user class
'''
class User(Model):
    '''
        init by simple setters
    '''
    def __init__(self, firstname, lastname, username, birthday, password, role):
        super(User, self).__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.birthday = birthday
        self.password = password
        self.role = role
        self.cart =[]

    '''
        print this class
    '''
    def print(self):
        print(f"ID: {self.entity_id}")
        print(f"First name: {self.firstname}")
        print(f"Last name: {self.lastname}")
        print(f"Birthday: {self.birthday}")
        print(f"Username: {self.username}")
        print(f"Passwort: {self.password}")

    '''
        add a product with amount to the user
    '''
    def add_to_cart(self, product, amount):
        self.cart.append((product, amount))

    '''
        calculate the whole bill
    '''
    def calc_bill(self):
        bill = 0
        for cart_item in self.cart:
            prod = cart_item[0]
            amount = cart_item[1]
            bill += prod.price_brutto * amount
        return bill

    '''
        reset the cart
    '''
    def reset_cart(self):
        self.cart = []
