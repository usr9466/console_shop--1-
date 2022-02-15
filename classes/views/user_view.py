from classes.views.view import View
from classes.models.User import User

'''
    the user view class
'''
class UserView(View):
    '''
        the init function of the user view
    '''
    def __init__(self):
        super(UserView,self).__init__('user')


    '''
        create a user
    '''
    def create_user(self):
        print("> What is your first name?")
        first_name = self.validate_input_loop("firstname")

        print("> What is your last name?")
        last_name = self.validate_input_loop("lastname")

        print("> What is your birthday?")
        birthday = self.validate_input_loop("birthday")

        print("> What is your prefered username?")
        username = self.validate_input_loop("birthday")

        print("> What is your password?")
        pw = self.validate_input_loop("password")

        print("> Thanks, we created a account for you!")
        return User(first_name, last_name, username, birthday, pw, "User")

    '''
        change the user
    '''
    def change_user(self,cur_acc):
        print("> Which attribute do you want to change? (firstname, lastname, birthday, username, password")
        done = False
        while not done:
            attribute = self.custom_input()
            if attribute in ["firstname", "lastname", "birthday", "username", "password"]:
                cur_acc = self.change_attribute(cur_acc, attribute)
                done = True
            else:
                print("> Not a valid attribute!")
        return cur_acc

    '''
        login is a getter with combined primary key: username, password <=> entity_id
    '''
    def login(self):
        while True:
            print("> Your Username:")
            username = self.custom_input()
            print("> Your Password:")
            pw = self.custom_input()
            return username, pw
            

    '''
        addd to card
    '''
    def add_to_cart(self,cur_acc, product_id2product):
        print("> Ok, please enter the product id you want to add to the cart")
        prod_id = self.custom_input()

        if prod_id not in product_id2product:
            print(f"> {prod_id} is not a valid Product ID!")
            return

        print(f"> How many products of {prod_id} you want to add to the cart?")
        amount = int(self.custom_input())

        if product_id2product[prod_id].in_stock >= amount:
            cur_acc.add_to_cart(product_id2product[prod_id], amount)
            print(f"> Ok, we added {amount} products of {prod_id} to your cart")
        else:
            print("> Sorry, there is not enough stock for this product")
        return cur_acc

    '''
        checkout the total bill
    '''
    def checkout(self,cur_acc):
        bill = cur_acc.calc_bill()
        print(f"> Ok. Your cart total is {bill} EUR")

        print("> What is your first name?")
        first_name = self.validate_input_loop("firstname")

        print("> What is your last name?")
        last_name = self.validate_input_loop("lastname")

        print("> What is the delivery adresse?")
        print("> Street: ")
        street = self.validate_input_loop("street")

        print("> Housenumber")
        housenumber = self.validate_input_loop("housenumber")

        print("> ZIP Code")
        zipcode = self.validate_input_loop("zip")

        print("> City")
        city = self.validate_input_loop("city")

        print("> Ok. Now we need your Credit Card details:")

        print("> Card Owner (first and second name")
        cc_name = self.validate_input_loop("credit_card_name")

        print("> Cred Card Number:")
        cc_number = self.validate_input_loop("credit_card_number")

        print("> CVV:")
        ccv = self.validate_input_loop("cvv")

        print("> Valid until (month)")
        cc_month = self.validate_input_loop("credit_card_valid_month")

        print("> Valid until (year)")
        cc_year = self.validate_input_loop("credit_card_valid_year")

        print("> Thank you for your order")
        return first_name, last_name, street, housenumber, zipcode, city, cc_name, cc_number, ccv, cc_month, cc_year