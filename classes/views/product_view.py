from classes.views.view import View
from classes.models.Product import Product


'''
    the product view class
'''
class ProductView(View):
    '''
        the init function of the product view
    '''
    def __init__(self):
        super(ProductView,self).__init__('product')

    '''
        create a product and add it tho the db
    '''
    def create_product(self):
        print("> Wie lautet der Name ihres Produktes?")
        prod_name = self.custom_input()

        print("> Wie lautet die beschreibung des Produktes?")
        prod_descr = self.custom_input()

        print("> Bitte setzen Sie den Preis ohne Steuern?")
        price_netto = self.custom_input()

        print("> Bitte setzen Sie den Preis inklusive Steuern?")
        price_brutto = self.custom_input()

        print("> Wie lautet die Produktkategorie?")
        prod_cat = self.custom_input()

        print("> Wie hoch ist die Anzahl der Produkte?")
        prod_stock = self.custom_input()

        prod = Product(prod_id, prod_name, prod_descr, price_netto, price_brutto, prod_stock, prod_cat)
        
        return prod