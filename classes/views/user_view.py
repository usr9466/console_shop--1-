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
        print("> Wie lautet ihr Vorname?")
        first_name = self.validate_input_loop("firstname")

        print("> Wie lautet ihr Nachname?")
        last_name = self.validate_input_loop("lastname")

        print("> Wann sind Sie geboren?")
        birthday = self.validate_input_loop("birthday")

        print("> Wie lautet ihr Benutzername?")
        username = self.validate_input_loop("birthday")

        print("> Wie soll ihr Passwort lauten?")
        pw = self.validate_input_loop("password")

        print("> Vielen Dank, Sie haben erfolgreich einen Benutzer angelegt!")
        return User(first_name, last_name, username, birthday, pw, "User")

    '''
        change the user
    '''
    def change_user(self,cur_acc):
        print("> Welches Attribute wollen Sie anpassen? Optionen: firstname, lastname, birthday, username, password")
        done = False
        while not done:
            attribute = self.custom_input()
            if attribute in ["firstname", "lastname", "birthday", "username", "password"]:
                cur_acc = self.change_attribute(cur_acc, attribute)
                done = True
            else:
                print("> Leider kein gültiges Attribut gefunden!")
        return cur_acc

    '''
        login is a getter with combined primary key: username, password <=> entity_id
    '''
    def login(self):
        print("> Benutzername:")
        username = self.custom_input()
        print("> Passwort:")
        pw = self.custom_input()
        return username, pw
            

    '''
        addd to card
    '''
    def add_to_cart(self,cur_acc, product_id2product):
        print("> Ok, bitte geben Sie die Produkt ID ein die Sie hinzufügen möchten")
        prod_id = self.custom_input()

        if prod_id not in product_id2product:
            print(f"> {prod_id} keine gültige Produkt ID!")
            return

        print(f"> Wie viele Produkte von {prod_id} möchten Sie ihrem Warenkorb hinzufügen?")
        amount = int(self.custom_input())

        if product_id2product[prod_id].in_stock >= amount:
            cur_acc.add_to_cart(product_id2product[prod_id], amount)
            print(f"> Ok, es wurden soeben {amount} Produkte mit der ID {prod_id} zu ihrem Warenkorb hinzugefügt")
        else:
            print("> Entschuldigung, wir haben leider nicht genug auf Lager...")
        return cur_acc

    '''
        checkout the total bill
    '''
    def checkout(self,cur_acc):
        bill = cur_acc.calc_bill()
        print(f"> Alles zusammen kostet {bill} EUR")

        print("> Wie lautet ihr Vorname?")
        first_name = self.validate_input_loop("firstname")

        print("> Wie lautet ihr Nachname?")
        last_name = self.validate_input_loop("lastname")

        print("> Wie lautet die Lieferadresse?")
        print("> Straße: ")
        street = self.validate_input_loop("street")

        print("> Hausnummer")
        housenumber = self.validate_input_loop("housenumber")

        print("> Postleitzahl")
        zipcode = self.validate_input_loop("zip")

        print("> Stadt")
        city = self.validate_input_loop("city")

        print("> Ok. Bitte die Kreditkarteninformation hinzufügen:")

        print("> Kartenbesitzer Angaben(Name & Kartennummer)")
        cc_name = self.validate_input_loop("credit_card_name")

        print(">Kartennummer:")
        cc_number = self.validate_input_loop("credit_card_number")

        print("> CVV:")
        ccv = self.validate_input_loop("cvv")

        print("> Gültig bis (Monat)")
        cc_month = self.validate_input_loop("credit_card_valid_month")

        print("> Gültig bis (Jahr)")
        cc_year = self.validate_input_loop("credit_card_valid_year")

        print("> Vielen Dank für ihre Bestellung")
        return first_name, last_name, street, housenumber, zipcode, city, cc_name, cc_number, ccv, cc_month, cc_year