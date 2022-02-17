from classes.views.view import View
from classes.views.product_view import ProductView
from classes.views.review_view import ReviewView
from classes.views.user_view import UserView
from classes.controllers.product_controller import ProductController
from classes.controllers.review_controller import ReviewController
from classes.controllers.user_controller import UserController
from classes.models.Product import Product
from classes.models.Review import Review
from classes.models.User import User


'''
    MainView class listen to the normal ui and menu inputs and holds all sub views and controllers
'''
class MainView(View):
    def __init__(self):
        super(MainView, self).__init__('main ui view')

        self.user_view = UserView()
        self.product_view = ProductView()
        self.review_view = ReviewView()
        self.user_controller = UserController()
        self.product_controller = ProductController()
        self.review_controller = ReviewController()

        print('START: backend initialisierung - Daten werden getestet...')
        
        admin_user = User("admin", "admin", "admin", "admin", "12345", "admin")
        test_user = User("tester_firstname", "tester_lastname", "tester", "1.1.2020", "12345", "user")
        products, reviews = self.generate_products()
        
        
        self.user_controller.post(admin_user)
        self.user_controller.post(test_user)

        for product in products.values():
            self.product_controller.post(product)
        
        for review in reviews.values():
            self.review_controller.post(review)


        print('END: initialize backend')

    '''
        generate the predefined products for testing
    '''    
    def generate_products(self):
        products = {}
        reviews = {}

        p1 = Product("Shampoo", "Smells like starwberries!", 4.3, 6.5, 120, "Bodyproducts")
        products[p1.entity_id] = p1
        self.add_to(reviews,Review("I lost all my hair!", "This shampoo is awefull, im bald now. 0/10, cant recommend!", p1.entity_id) )
        self.add_to(reviews, Review("Smells awesome!", "I love the smell of strawberries!", p1.entity_id))

        p2 = Product("Scissors", "Cuts everything, literally everything", 2.1, 3.2, 15, "household items")
        products[p2.entity_id] = p2 

        p3 = Product("TV", "Curve screen TV", 388, 518, 12, "electronics")
        products[p3.entity_id] = p3

        self.add_to(reviews,Review("Great pictures", "Love those 120 FPS",p3.entity_id))
        self.add_to(reviews,Review("Sound is odd", "Sound is very bad, might be malfunctioning", p3.entity_id))

        p4 = Product("Football", "Standard sized football", 4.0, 6.0, 20, "sports")
        products[p4.entity_id] = p4
        self.add_to(reviews,Review("Broke my leg", "Tripped over it and broke my leg, cant be my fault", p4.entity_id))
        self.add_to(reviews,Review("Score!", "First ball i was ever able to score with, awesome!", p4.entity_id))


        p5 = Product("Book", "Plain, old book", 2.0, 4.0, 27, "books")
        products[p5.entity_id] = p5 

        p6 = Product("Parfume", "You are gonna smell like a champ!", 47.0, 61.0, 999, "parfumes")
        products[p6.entity_id] = p6 
        self.add_to(reviews,Review("Literally smelled like a champ..",
                            "I didnt know that this was meant literally, i smelled extremly sweaty because of it..", p6.entity_id))

        p7 = Product("Guitare", "For your very own garage band!", 134.0, 161.0, 3, "musical instruments")
        products[p7.entity_id] = p7

        p8 = Product( "PC Screen", "12 Inch PC screen!", 150.0, 170.0, 74, "electronics")
        products[p8.entity_id] = p8 

        p9 = Product( "Trash can", "Can store up to 12 liters of trash", 8.0, 11.0, 13, "household items")
        products[p9.entity_id] = p9 
        self.add_to(reviews,Review("Amazing volume", "I can put so much trash in this, its amazing", p9.entity_id))

        p10 = Product("Snickers", "Delicious chocolate bar", 1.5, 1.8, 420, "snacks")
        products[p10.entity_id] = p10 

        return products, reviews
    
    '''
        helper function
    '''
    def add_to(self, list, object):
        list[object.entity_id] = object

    def print_actions(self):
        print("********************************************")
        print("> createAccount - Account erstellen")
        print("> login - Benutzer login")
        print("> viewAccount -  Account Details ausgeben")
        print("> changeUser - Nutzer ändern")
        print("> viewProducts - Produktliste anzeigen")
        print("> addProduct - Produkt hinzufügen")
        print("> addToCart -  Produkt dem Warenkorb hinzufügen")
        print("> viewReviews - Kundenbewertung anzeigen")
        print("> checkout - Warenkorb auschecken")
        print("> writeReview - Kundenbewertung schreiben")
        print("> logout - Nutzer ausloggen")
        print("********************************************")



    '''
        this is the main shop loop
        we provide the user interface by string input
    '''
    def main_loop(self):
        cur_user = None
        while True:
            print("> Welche Aktion möchten Sie vornehemen?")
            self.print_actions()
            action = self.custom_input()
            if action == "createAccount":
                new_acc = self.user_view.create_user()
                self.user_controller.post(new_acc)
                cur_user = new_acc
            elif action == "login":
                possible_username, possible_password =  self.user_view.login()
                cur_user = self.user_controller.login(possible_username, possible_password)
                if(not cur_user): print("error during login")
                else:
                    print("eingeloggt mit User: " + cur_user.username)
            elif action == "viewAccount":
                if cur_user is None:
                    print("> Bitte zuerst einen Account anlegen/Nutzer erstellen!")
                else:
                    cur_user.print()
            elif action == "changeUser":
                if cur_user is None:
                    print("> Bitte einloggen oder falls nicht geschehen einen Account anlegen!")
                else:
                    cur_user = self.user_view.change_user(cur_user)
                    self.user_controller.put(cur_user.entity_id,cur_user)
            elif action == "viewProducts":
                i = 0
                for product in self.product_controller.get_all():
                    print(f"> Produkt: {i}")
                    i += 1
                    product.describe()
            elif action == "addProduct":
                if cur_user.role == "admin":
                    newProduct = self.product_view.create_product()
                    self.product_controller.post(newProduct)
                    print("Check -  Produkt erfolgreich angelegt: ")
                    newProduct.describe()
                else:
                    print("> Bitte mit Admin Rechten anmelden, User können keine Produkte anlegen")
            elif action == "addToCart":
                if cur_user is None:
                    print("> Bitte einloggen oder falls nicht geschehen einen Account anlegen!")
                else:
                    updated_user = self.user_view.add_to_cart(cur_user, self.product_controller.get_dict())
                    self.user_controller.put(updated_user.entity_id, updated_user)
            elif action == "viewReviews":
                product_dict = self.product_controller.get_dict()
                reviews = self.review_controller.get_all()
                self.review_view.view_reviews(product_dict, reviews)
            elif action == "checkout":
                if cur_user == None:
                    print("> Sie müssen angemeldet sein um einen Checkout zu machen!")
                else:
                    self.user_view.checkout(cur_user)
                    cur_user.reset_cart()
                    self.user_controller.put(cur_user.entity_id, cur_user)
            elif action == "writeReview":
                if cur_user == None:
                    print("> Sie müssen angemeldet sein um eine Kundenbewertung zu schreiben!")
                else:
                    product_dict = self.product_controller.get_dict()
                    rev = self.review_view.write_review(product_dict)
                    response = self.review_controller.post(rev)
            elif action == "logout":
                cur_user = None
                print("> Erfolgreich ausgeloggt!")
            else:
                print("> Unbekannte Funktion -  bitte nochmal eingeben..!")

