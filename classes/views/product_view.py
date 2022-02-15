from view import View
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
        print("> What is the name of the product?")
        prod_name = self.custom_input()

        print("> What is the product description?")
        prod_descr = self.custom_input()

        print("> What is the price excluding taxes?")
        price_netto = self.custom_input()

        print("> What is the price including taxes?")
        price_brutto = self.custom_input()

        print("> What is the category of the product?")
        prod_cat = self.custom_input()

        print("> What is the stock?")
        prod_stock = self.custom_input()

        prod = Product(prod_id, prod_name, prod_descr, price_netto, price_brutto, prod_stock, prod_cat)
        
        return prod