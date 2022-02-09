class Product:
    def __init__(self, product_id, name, description, price_netto, price_brutto, in_stock, category):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price_netto = price_netto
        self.price_brutto = price_brutto
        self.in_stock = in_stock
        self.category = category

    def describe(self):
        print(f"> ID: {self.product_id}")
        print(f"> Name: {self.name}")
        print(f"> Description: {self.description}")
        print(f"> Preis exl. tax: {self.price_netto}")
        print(f"> Preis incl. tax: {self.price_brutto}")
        print(f"> Stock: {self.in_stock}")
        print(f"> Category: {self.category}")
        print()
