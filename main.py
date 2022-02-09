from classes.User import *
from classes.Product import *
from classes.Review import *


def custom_input():
    val = input()
    if val == "quit":
        exit(0)
    else:
        return val


def create_account(user_id):
    print("> What is your first name?")
    first_name = validate_input_loop("firstname")

    print("> What is your last name?")
    last_name = validate_input_loop("lastname")

    print("> What is your birthday?")
    birthday = validate_input_loop("birthday")

    print("> What is your prefered username?")
    username = validate_input_loop("birthday")

    print("> What is your password?")
    pw = validate_input_loop("password")

    print("> Thanks, we created a account for you!")
    return User(user_id, first_name, last_name, username, birthday, pw, "User")


def change_user(cur_acc):
    print("> Which attribute do you want to change? (firstname, lastname, birthday, username, password")
    done = False
    while not done:
        attribute = custom_input()
        if attribute in ["firstname", "lastname", "birthday", "username", "password"]:
            cur_acc = change_attribute(cur_acc, attribute)
            done = True

        else:
            print("> Not a valid attribute!")


def change_attribute(cur_acc, attribute):

    if attribute == "firstname":
        print("> Your new firstname:")
        user_input = validate_input_loop("firstname")
        print("> Ok, we changed your first name")
    if attribute == "lastname":
        print("> Your new lastname:")
        user_input = validate_input_loop("lastname")
        print("> Ok, we changed your last name")
    if attribute == "birthday":
        print("> Your new birthday:")
        user_input = validate_input_loop("birthday")
        print("> Ok, we changed your birthday")
    if attribute == "username":
        print("> Your new username:")
        user_input = validate_input_loop("username")
        print("> Ok, we changed your username")
    if attribute == "password":
        print("> Your new password:")
        user_input = validate_input_loop("password")
        print("> Ok, we changed your password")

    setattr(cur_acc, attribute, user_input)


def validate_input_loop(typ):
    valid_input = False
    while not valid_input:
        value = custom_input()
        valid_input, response = input_validation(value, typ)
        if not valid_input:
            print(response)

    return value


def input_validation(user_input, typ):
    # input validation for all kinds of user inputs, returns (bool, output), output only important if not valid

    if typ == "firstname":
        if len(user_input) >= 3 and user_input[0].isupper():
            return True, "valid"
        else:
            return False, "> Sorry, your firstname must have at least 3 characters and start with an uppercase letter. Please enter a new one"

    if typ == "lastname":
        if len(user_input) >= 3 and user_input[0].isupper():
            return True, "valid"
        else:
            return False, "> Sorry, your lastname must have at least 3 characters and start with an uppercase letter. Please enter a new one"

    if typ == "password":
        if len(user_input) >= 8:
            print()
            if (any(x.isupper() for x in user_input) and any(x.islower() for x in user_input)
                    and any(x.isdigit() for x in user_input)):
                return True, "valid"
            else:
                return False, "> Sorry, your password must contain an upper-case letter, a lower-case letter and a number! Please enter a new one"
        else:
            return False, "> Sorry your password is to short, it must have at least 8 characters"

    if typ == "username":
        if len(user_input) > 0:
            return True, "valid"
        else:
            return False, "> Sorry, your username must have at least 1 character. Please enter a new one"


    if typ == "birthday":
        if len(user_input) > 0:
            return True, "valid"
        else:
            return False, "> Sorry, your birthday must have at least 1 character. Please enter a new one"

    if typ == "street":
        if len(user_input) >= 3 and user_input[0].isupper():
            return True, "valid"
        else:
            return False, "> Sorry, your street must have at least 3 characters and start with an uppercase letter. Please enter a new one"

    if typ == "housenumber":
        if len(user_input) > 0 and user_input.isdigit():
            return True, "valid"
        else:
            return False, "> Sorry, your housenumber can only include digits and cant be emtpy! Please enter a new one"

    if typ == "city":
        if len(user_input) >= 3 and user_input[0].isupper():
            return True, "valid"
        else:
            return False, "> Sorry, your city must have at least 3 characters and start with an uppercase letter. Please enter a new one"

    if typ == "zip":
        if len(user_input) == 5 and user_input.isdigit():
            return True, "valid"
        else:
            return False, "> Sorry, your zip code has to be exactly 5 digits! Please enter a new one"

    if typ == "credit_card_name":
        if len(user_input) >= 6 and any(x.isspace() for x in user_input):
            return True, "valid"
        else:
            return False, "> Sorry, your Credit Card Name must be at least 6 characters and conatain a whitespace seperator between first- and lastname! Please enter a new one"

    if typ == "credit_card_number":
        user_input = user_input.replace(" ", "")
        if len(user_input) == 16 and user_input.isdigit():
            return True, "valid"
        else:
            return False, "> Sorry, your Credit Card Number must contain exactly 16 digits! Please enter a new one"

    if typ == "cvv":
        if len(user_input) == 3 and user_input.isdigit():
            return True, "valid"
        else:
            return False, "> Sorry, your Credit Card CVV must contain exactly 3 digits! Please enter a new one"

    if typ == "credit_card_valid_month":
        if user_input.isdigit() and 1 <= int(user_input) <= 12:
            return True, "valid"
        else:
            return False, "> Sorry, your credit card valid until month has to be a digit between 1 and 12. Please enter a new one"

    if typ == "credit_card_valid_year":
        if user_input.isdigit() and int(user_input) >= 2020:
            return True, "valid"
        else:
            return False, "> Sorry, your credit card valid until year has to be a digit larger than 2020. Please enter a new one"

    if typ == "review_heading":
        if len(user_input) >= 3:
            return True, "valid"
        else:
            return False, "> Sorry, your review heading has to be longer than 3 characters. Please enter a new one"

    if typ == "review_text":
        if len(user_input) >= 3:
            return True, "valid"
        else:
            return False, "> Sorry, your review text has to be longer than 3 characters. Please enter a new one"


def generate_products():
    products = {}
    reviews = []

    products["P101"] = Product("P101", "Shampoo", "Smells like starwberries!", 4.3, 6.5, 120, "Bodyproducts")
    reviews.append(Review("0", "I lost all my hair!", "This shampoo is awefull, im bald now. 0/10, cant recommend!", "P101"))
    reviews.append(Review("1", "Smells awesome!", "I love the smell of strawberries!", "P101"))

    products["Z1111"] = Product("Z1111", "Scissors", "Cuts everything, literally everything", 2.1, 3.2, 15, "household items")

    products["E1234"] = Product("E1234", "TV", "Curve screen TV", 388, 518, 12, "electronics")
    reviews.append(Review("2", "Great pictures", "Love those 120 FPS", "E1234"))
    reviews.append(Review("3", "Sound is odd", "Sound is very bad, might be malfunctioning", "E1234"))

    products["P3001"] = Product("P3001", "Football", "Standard sized football", 4.0, 6.0, 20, "sports")
    reviews.append(Review("4", "Broke my leg", "Tripped over it and broke my leg, cant be my fault", "P3001"))
    reviews.append(Review("5", "Score!", "First ball i was ever able to score with, awesome!", "P3001"))

    products["401Z12"] = Product("401Z12", "Book", "Plain, old book", 2.0, 4.0, 27, "books")

    products["Z500"] = Product("Z500", "Parfume", "You are gonna smell like a champ!", 47.0, 61.0, 999, "parfumes")
    reviews.append(Review("6", "Literally smelled like a champ..",
                          "I didnt know that this was meant literally, i smelled extremly sweaty because of it..", "Z500"))

    products["X601"] = Product("X601", "Guitare", "For your very own garage band!", 134.0, 161.0, 3, "musical instruments")

    products["700123"] = Product("700123", "PC Screen", "12 Inch PC screen!", 150.0, 170.0, 74, "electronics")

    products["N801"] = Product("N801", "Trash can", "Can store up to 12 liters of trash", 8.0, 11.0, 13, "household items")
    reviews.append(Review("7", "Amazing volume", "I can put so much trash in this, its amazing", "N801"))

    products["ZT109"] = Product("ZT109", "Snickers", "Delicious chocolate bar", 1.5, 1.8, 420, "snacks")

    return products, reviews


def login(username2user):
    while True:
        print("> Your Username:")
        username = custom_input()
        print("> Your Password:")
        pw = custom_input()

        if username in username2user:
            if pw == username2user[username].password:
                print("> You are logged in!")
                return username2user[username]
            else:
                print("> Wrong password!")

        else:
            print("> Username not registered")


def create_product():
    print("> What is the product id?")
    prod_id = custom_input()

    print("> What is the name of the product?")
    prod_name = custom_input()

    print("> What is the product description?")
    prod_descr = custom_input()

    print("> What is the price excluding taxes?")
    price_netto = custom_input()

    print("> What is the price including taxes?")
    price_brutto = custom_input()

    print("> What is the category of the product?")
    prod_cat = custom_input()

    print("> What is the stock?")
    prod_stock = custom_input()

    prod = Product(prod_id, prod_name, prod_descr, price_netto, price_brutto, prod_stock, prod_cat)

    return prod


def add_to_cart(cur_acc, product_id2product):
    print("> Ok, please enter the product id you want to add to the cart")
    prod_id = custom_input()

    if prod_id not in product_id2product:
        print(f"> {prod_id} is not a valid Product ID!")
        return

    print(f"> How many products of {prod_id} you want to add to the cart?")
    amount = int(custom_input())

    if product_id2product[prod_id].in_stock >= amount:
        cur_acc.add_to_cart(product_id2product[prod_id], amount)
        print(f"> Ok, we added {amount} products of {prod_id} to your cart")
    else:
        print("> Sorry, there is not enough stock for this product")


def view_reviews(product_id2product, reviews):
    print("> For which product do you want to see the reviews?")
    prod_id = custom_input()

    if prod_id in product_id2product:
        print(f"> Here are the reviews for {prod_id}")
        i = 1
        for review in reviews:
            if review.product_id == prod_id:
                print(f"> Review {i}:")
                review.print()
                print("")
                i += 1

    else:
        print(f"> {prod_id} is not a valid Product ID!")


def checkout(cur_acc):
    bill = cur_acc.calc_bill()
    print(f"> Ok. Your cart total is {bill} EUR")

    print("> What is your first name?")
    first_name = validate_input_loop("firstname")

    print("> What is your last name?")
    last_name = validate_input_loop("lastname")

    print("> What is the delivery adresse?")
    print("> Street: ")
    street = validate_input_loop("street")

    print("> Housenumber")
    housenumber = validate_input_loop("housenumber")

    print("> ZIP Code")
    zipcode = validate_input_loop("zip")

    print("> City")
    city = validate_input_loop("city")

    print("> Ok. Now we need your Credit Card details:")

    print("> Card Owner (first and second name")
    cc_name = validate_input_loop("credit_card_name")

    print("> Cred Card Number:")
    cc_number = validate_input_loop("credit_card_number")

    print("> CVV:")
    ccv = validate_input_loop("cvv")

    print("> Valid until (month)")
    cc_month = validate_input_loop("credit_card_valid_month")

    print("> Valid until (year)")
    cc_year = validate_input_loop("credit_card_valid_year")

    print("> Thank you for your order")


def write_review(product_id2product):
    print("> Ok. For which product do you want to write a review?")
    prod_id = custom_input()

    if prod_id in product_id2product:
        print("> Please enter the heading of the review")
        heading = validate_input_loop("review_heading")

        print("> Please enter your review")
        review_text = validate_input_loop("review_text")

        review = Review(len(reviews), heading, review_text, prod_id)
        print("> Ok, we saved the review")
        return review

    else:
        print("> Sorry we couldn't find the product!")
        return -1


if __name__ == '__main__':
    username2user = {}
    product_id2product, reviews = generate_products()

    username2user['admin'] = User(len(username2user), "admin", "admin", "admin", "admin", "12345", "admin")
    username2user['tester'] = User(len(username2user), "tester_firstname", "tester_lastname", "tester", "1.1.2020", "12345", "user")

    cur_user = None
    # input loop
    while True:
        print("> What do you want to do?")
        action = custom_input()

        if action == "createAccount":
            new_acc = create_account(len(username2user))
            username2user[new_acc.username] = new_acc
            cur_user = new_acc

        elif action == "login":
            cur_user = login(username2user)

        elif action == "viewAccount":
            if cur_user is None:
                print("> Sorry you have to login or create a new account first!")
            else:
                cur_user.print()

        elif action == "changeUser":
            if cur_user is None:
                print("> Sorry you have to login or create a new account first!")
            else:
                change_user(cur_user)

        elif action == "viewProducts":
            i = 0
            for product_id in product_id2product:
                print(f"> Product {i}")
                i += 1
                product_id2product[product_id].describe()

        elif action == "addProduct":
            if cur_user.role == "admin":
                newProduct = create_product()
                print("Ok. We created a new product: ")
                newProduct.describe()
                product_id2product[newProduct.product_id] = newProduct
            else:
                print("> Sorry, you are no admin, Only admins can add new products")

        elif action == "addToCart":
            if cur_user is None:
                print("> Sorry you have to login or create a new account first!")
            else:
                add_to_cart(cur_user, product_id2product)

        elif action == "viewReviews":
            view_reviews(product_id2product, reviews)

        elif action == "checkout":
            checkout(cur_user)

        elif action == "writeReview":
            rev = write_review(product_id2product)
            if rev != -1:
                reviews.append(rev)

        elif action == "logout":
            cur_user = None
            print("> You are logged out!")

        else:
            print("> Unkown action!")
