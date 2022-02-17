import numpy as np


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
                return False, "> Eingabefehler, ist Vorname muss min. 3 Zeichen lang sein und mit einem Großbuchstabe anfangen. Bitte nochmal eingeben"

        if type == "lastname":
            if len(user_input) >= 3 and user_input[0].isupper():
                return True, "valid"
            else:
                return False, "> Eingabefehler, ist Nachname muss min. 3 Zeichen lang sein und mit einem Großbuchstabe anfangen. Bitte nochmal eingeben"

        if type == "password":
            if len(user_input) >= 8:
                print()
                if (any(x.isupper() for x in user_input) and any(x.islower() for x in user_input)
                        and any(x.isdigit() for x in user_input)):
                    return True, "valid"
                else:
                    return False, "> Eingabefehler, ihr Passwort muss einen Großbuchstabe, einen Kleinbuchstabe und mindestens eine Nummer enthalten"
            else:
                return False, "> Eingabefehler, ihr Passwort ist zu kurz es muss mindestens 8 Zeichen lang sein"

        if type == "username":
            if len(user_input) > 0:
                return True, "valid"
            else:
                return False, "> Eingabefehler, ihr Benutzername muss mindestens 1 Zeichen lang sein. Bitte erneut eingeben"


        if type == "birthday":
            if len(user_input) > 0:
                return True, "valid"
            else:
                return False, "> Eingabefehler, ihr Geburtsdatum muss mindesten 1 Zeichen lang sein. Bitte erneut eingeben"

        if type == "street":
            if len(user_input) >= 3 and user_input[0].isupper():
                return True, "valid"
            else:
                return False, "> Eingabefehler, ihre Straße muss mindestens 3 Zeichen lang sein und mit einem Großbuchstabe anfangen. Bitte erneut eingeben"

        if type == "housenumber":
            if len(user_input) > 0 and user_input.isdigit():
                return True, "valid"
            else:
                return False, "> Eingabefehler, die Hausnummer kann nur Zahlen enthalten und darf nicht leer sein. Bitte erneut eingeben"

        if type == "city":
            if len(user_input) >= 3 and user_input[0].isupper():
                return True, "valid"
            else:
                return False, "> Eingabefehler, die Stadt muss mindesten 3 Zeichen lang sein und mit einem Großbuchstabe anfangen. Bitte erneut eingeben"

        if type == "zip":
            if len(user_input) == 5 and user_input.isdigit():
                return True, "valid"
            else:
                return False, "> Eingabefehler, die Postleitzahl muss genau 5 Zahlen enthalten. Bitte erneut eingeben"

        if type == "credit_card_name":
            if len(user_input) >= 6 and any(x.isspace() for x in user_input):
                return True, "valid"
            else:
                return False, "> Eingabefehler, der Kreditkartenname muss mindestens 6 Zeichen lang sein und ein Leerzeichen zwischen Vor- und Nachname enthalten. Bitte erneut eingeben"

        if type == "credit_card_number":
            user_input = user_input.replace(" ", "")
            if len(user_input) == 16 and user_input.isdigit():
                return True, "valid"
            else:
                return False, "> Eingabefehler, die Kreditkartennummer muss genau 16 Zahlen enthalten. Bitte erneut eingeben"

        if type == "cvv":
            if len(user_input) == 3 and user_input.isdigit():
                return True, "valid"
            else:
                return False, "> Eingabefehler, die Kreditkartencode muss genau 3 Zahlen enthalten. Bitte erneut eingeben"

        if type == "credit_card_valid_month":
            if user_input.isdigit() and 1 <= int(user_input) <= 12:
                return True, "valid"
            else:
                return False, "> Eingabefehler, die Angabe des Monats muss eine Zahl zwischen 1 und 12 enthalten. Bitte erneut eingeben"

        if type == "credit_card_valid_year":
            if user_input.isdigit() and int(user_input) >= 2020:
                return True, "valid"
            else:
                return False, "> Eingabefehler, die Angabe der Jahres muss größer gleich 2020 sein"

        if type == "review_heading":
            if len(user_input) >= 3:
                return True, "valid"
            else:
                return False, "> Eingabefehler, die Überschrift ihrer Bewertung muss mehr als 3 Zeichen entahlten. Bitte erneut eingeben"

        if type == "review_text":
            if len(user_input) >= 3:
                return True, "valid"
            else:
                return False, "> Eingabefehler, der Text der Bewertung muss mehr als 3 Zeichen entahlten. Bitte erneut eingeben"


    '''
        change an attribute from a 
    '''
    def change_attribute(self,cur_obj, attribute):
        if attribute == "firstname":
            print("> Neuer Vorname:")
            user_input = self.validate_input_loop("firstname")
            print("> Ok, Vorname wurde geändert")
        if attribute == "lastname":
            print("> Neuer Nachname:")
            user_input = self.validate_input_loop("lastname")
            print("> Ok, Nachname wurde geändert")
        if attribute == "birthday":
            print("> Neues Geburtsdatum:")
            user_input = self.validate_input_loop("birthday")
            print("> Ok, Geburtsdatum wurde geändert")
        if attribute == "username":
            print("> Neuer Benutzername:")
            user_input = self.validate_input_loop("username")
            print("> Ok, Benutzername wurde geändert")
        if attribute == "password":
            print("> Neues Passwort:")
            user_input = self.validate_input_loop("password")
            print("> Ok, Passwort wurde geändert")
        setattr(cur_obj, attribute, user_input)