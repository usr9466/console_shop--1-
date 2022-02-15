from curses import curs_set
import imp
from view import View
from product_view import ProductView
from review_view import ReviewView
from user_view import UserView

from controllers.product_controller import ProductController
from controllers.review_controller import ReviewController
from controllers.user_controller import UserController

from models.Product import Product
from models.Review import Review
from models.User import User


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

        print('START: initialize backend : testing data ')
        
        admin_user = User("admin", "admin", "admin", "admin", "12345", "admin")
        test_user = User("tester_firstname", "tester_lastname", "tester", "1.1.2020", "12345", "user")
        products, reviews = self.generate_products()
        
        
        self.user_controller.post(admin_user)
        self.user_controller.post(test_user)

        for product in products:
            self.product_controller.post(product)
        
        for review in reviews:
            self.review_controller.post(review)


        print('END: initialize backend')

    '''
        generate the predefined products for testing
    '''    
    def generate_products():
        products = {}
        reviews = []

        products["P101"] = Product("Shampoo", "Smells like starwberries!", 4.3, 6.5, 120, "Bodyproducts")
        reviews.append(Review("I lost all my hair!", "This shampoo is awefull, im bald now. 0/10, cant recommend!", "P101"))
        reviews.append(Review("Smells awesome!", "I love the smell of strawberries!", "P101"))

        products["Z1111"] = Product("Scissors", "Cuts everything, literally everything", 2.1, 3.2, 15, "household items")

        products["E1234"] = Product("TV", "Curve screen TV", 388, 518, 12, "electronics")
        reviews.append(Review("Great pictures", "Love those 120 FPS", "E1234"))
        reviews.append(Review("Sound is odd", "Sound is very bad, might be malfunctioning", "E1234"))

        products["P3001"] = Product("Football", "Standard sized football", 4.0, 6.0, 20, "sports")
        reviews.append(Review("Broke my leg", "Tripped over it and broke my leg, cant be my fault", "P3001"))
        reviews.append(Review("Score!", "First ball i was ever able to score with, awesome!", "P3001"))

        products["401Z12"] = Product("Book", "Plain, old book", 2.0, 4.0, 27, "books")

        products["Z500"] = Product("Parfume", "You are gonna smell like a champ!", 47.0, 61.0, 999, "parfumes")
        reviews.append(Review("Literally smelled like a champ..",
                            "I didnt know that this was meant literally, i smelled extremly sweaty because of it..", "Z500"))

        products["X601"] = Product("Guitare", "For your very own garage band!", 134.0, 161.0, 3, "musical instruments")

        products["700123"] = Product( "PC Screen", "12 Inch PC screen!", 150.0, 170.0, 74, "electronics")

        products["N801"] = Product( "Trash can", "Can store up to 12 liters of trash", 8.0, 11.0, 13, "household items")
        reviews.append(Review("Amazing volume", "I can put so much trash in this, its amazing", "N801"))

        products["ZT109"] = Product("Snickers", "Delicious chocolate bar", 1.5, 1.8, 420, "snacks")

        return products, reviews
    

    '''
        this is the main shop loop
        we provide the user interface by string input
    '''
    def main_loop(self):
        cur_user = None
        while True:
            print("> What do you want to do?")
            action = self.custom_input()

            if action == "createAccount":
                new_acc = self.user_view.create_user()
                self.user_controller.post(new_acc)
                cur_user = new_acc

            elif action == "login":
                possible_username, possible_password =  self.user_view.login()
                cur_user = self.user_controller.login(possible_username, possible_password)

            elif action == "viewAccount":
                if cur_user is None:
                    print("> Sorry you have to login or create a new account first!")
                else:
                    cur_user.print()

            elif action == "changeUser":
                if cur_user is None:
                    print("> Sorry you have to login or create a new account first!")
                else:
                    cur_user = self.user_view.change_user(cur_user)
                    self.user_controller.put(cur_user.entity_id,cur_user)

            elif action == "viewProducts":
                i = 0
                for product in self.product_controller.get_all():
                    print(f"> Product {i}")
                    i += 1
                    product.describe()

            elif action == "addProduct":
                if cur_user.role == "admin":
                    newProduct = self.product_view.create_product()
                    self.product_controller.post(newProduct)
                    print("Ok. We created a new product: ")
                    newProduct.describe()
                else:
                    print("> Sorry, you are no admin, Only admins can add new products")

            elif action == "addToCart":
                if cur_user is None:
                    print("> Sorry you have to login or create a new account first!")
                else:
                    updated_user = self.user_view.add_to_cart(cur_user, self.product_controller.get_dict())
                    self.user_controller.put(updated_user.entity_id, updated_user)

            elif action == "viewReviews":
                product_dict = self.product_controller.get_dict()
                reviews = self.review_controller.get_all()
                self.review_view.view_reviews(product_dict, reviews)

            elif action == "checkout":
                if cur_user == None:
                    print("> Sorry you have to login to checkout!")
                else:
                    self.user_view.checkout(cur_user)
                    cur_user.reset_cart()
                    self.user_controller.put(cur_user.entity_id, cur_user)
            elif action == "writeReview":
                if cur_user == None:
                    print("> Sorry you have to login to write a review!")
                else:
                    product_dict = self.product_controller.get_dict()
                    rev = self.review_view.write_review(product_dict)
                    response = self.review_controller.post(rev)
            elif action == "logout":
                cur_user = None
                print("> You are logged out!")
            else:
                print("> Unkown action!")

