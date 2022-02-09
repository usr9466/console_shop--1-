class User:
    def __init__(self, user_id, firstname, lastname, username, birthday, password, role):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.birthday = birthday
        self.password = password
        self.role = role
        self.cart = []

    def print(self):
        print(f"First name: {self.firstname}")
        print(f"Last name: {self.lastname}")
        print(f"Birthday: {self.birthday}")
        print(f"Username: {self.username}")
        print(f"Passwort: {self.password}")

    def add_to_cart(self, product, amount):
        self.cart.append((product, amount))

    def calc_bill(self):
        bill = 0
        for cart_item in self.cart:
            prod = cart_item[0]
            amount = cart_item[1]
            bill += prod.price_brutto * amount

        return bill
