

'''
    the base view class
    we use this class to manage some basic print functions

'''
class View():
    '''
        the initialize method
        :param name is type of string and reference the name of the view
    '''
    def __init__(self, name):
        super(View, self).__init__()
        self.name = name # assign the name

    '''
        return the input of the user
    '''
    def custom_input(self):
        try:
            val = input()
            if val == "quit":
                exit(0)
            else:
                return val
        except:
            print('error in custom input')


    '''
        validate an input
    '''
    def validate_input_loop(self,typ):
        valid_input = False
        while not valid_input:
            value = self.custom_input()
            valid_input, response = self.input_validation(value, typ)
            if not valid_input:
                print(response)

        return value

    
    '''
        validate all kind of inputs
        param user_input: the input from user
        param type : form type
    '''
    def input_validation(self,user_input, type):
        # input validation for all kinds of user inputs, returns (bool, output), output only important if not valid

        if type == "firstname":
            if len(user_input) >= 3 and user_input[0].isupper():
                return True, "valid"
            else:
                return False, "> Sorry, your firstname must have at least 3 characters and start with an uppercase letter. Please enter a new one"

        if type == "lastname":
            if len(user_input) >= 3 and user_input[0].isupper():
                return True, "valid"
            else:
                return False, "> Sorry, your lastname must have at least 3 characters and start with an uppercase letter. Please enter a new one"

        if type == "password":
            if len(user_input) >= 8:
                print()
                if (any(x.isupper() for x in user_input) and any(x.islower() for x in user_input)
                        and any(x.isdigit() for x in user_input)):
                    return True, "valid"
                else:
                    return False, "> Sorry, your password must contain an upper-case letter, a lower-case letter and a number! Please enter a new one"
            else:
                return False, "> Sorry your password is to short, it must have at least 8 characters"

        if type == "username":
            if len(user_input) > 0:
                return True, "valid"
            else:
                return False, "> Sorry, your username must have at least 1 character. Please enter a new one"


        if type == "birthday":
            if len(user_input) > 0:
                return True, "valid"
            else:
                return False, "> Sorry, your birthday must have at least 1 character. Please enter a new one"

        if type == "street":
            if len(user_input) >= 3 and user_input[0].isupper():
                return True, "valid"
            else:
                return False, "> Sorry, your street must have at least 3 characters and start with an uppercase letter. Please enter a new one"

        if type == "housenumber":
            if len(user_input) > 0 and user_input.isdigit():
                return True, "valid"
            else:
                return False, "> Sorry, your housenumber can only include digits and cant be emtpy! Please enter a new one"

        if type == "city":
            if len(user_input) >= 3 and user_input[0].isupper():
                return True, "valid"
            else:
                return False, "> Sorry, your city must have at least 3 characters and start with an uppercase letter. Please enter a new one"

        if type == "zip":
            if len(user_input) == 5 and user_input.isdigit():
                return True, "valid"
            else:
                return False, "> Sorry, your zip code has to be exactly 5 digits! Please enter a new one"

        if type == "credit_card_name":
            if len(user_input) >= 6 and any(x.isspace() for x in user_input):
                return True, "valid"
            else:
                return False, "> Sorry, your Credit Card Name must be at least 6 characters and conatain a whitespace seperator between first- and lastname! Please enter a new one"

        if type == "credit_card_number":
            user_input = user_input.replace(" ", "")
            if len(user_input) == 16 and user_input.isdigit():
                return True, "valid"
            else:
                return False, "> Sorry, your Credit Card Number must contain exactly 16 digits! Please enter a new one"

        if type == "cvv":
            if len(user_input) == 3 and user_input.isdigit():
                return True, "valid"
            else:
                return False, "> Sorry, your Credit Card CVV must contain exactly 3 digits! Please enter a new one"

        if type == "credit_card_valid_month":
            if user_input.isdigit() and 1 <= int(user_input) <= 12:
                return True, "valid"
            else:
                return False, "> Sorry, your credit card valid until month has to be a digit between 1 and 12. Please enter a new one"

        if type == "credit_card_valid_year":
            if user_input.isdigit() and int(user_input) >= 2020:
                return True, "valid"
            else:
                return False, "> Sorry, your credit card valid until year has to be a digit larger than 2020. Please enter a new one"

        if type == "review_heading":
            if len(user_input) >= 3:
                return True, "valid"
            else:
                return False, "> Sorry, your review heading has to be longer than 3 characters. Please enter a new one"

        if type == "review_text":
            if len(user_input) >= 3:
                return True, "valid"
            else:
                return False, "> Sorry, your review text has to be longer than 3 characters. Please enter a new one"


    '''
        change an attribute from a 
    '''
    def change_attribute(self,cur_obj, attribute):
        if attribute == "firstname":
            print("> Your new firstname:")
            user_input = self.validate_input_loop("firstname")
            print("> Ok, we changed your first name")
        if attribute == "lastname":
            print("> Your new lastname:")
            user_input = self.validate_input_loop("lastname")
            print("> Ok, we changed your last name")
        if attribute == "birthday":
            print("> Your new birthday:")
            user_input = self.validate_input_loop("birthday")
            print("> Ok, we changed your birthday")
        if attribute == "username":
            print("> Your new username:")
            user_input = self.validate_input_loop("username")
            print("> Ok, we changed your username")
        if attribute == "password":
            print("> Your new password:")
            user_input = self.validate_input_loop("password")
            print("> Ok, we changed your password")
        #TODO: check other changes (product, review)
        setattr(cur_obj, attribute, user_input)