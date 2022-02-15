from classes.models.model import Model

class Review(Model):
    def __init__(self, headline, text, product_id):
        super(Review,self).__init__()
        self.headline = headline
        self.text = text
        self.product_id = product_id

    def print(self):
        print(f"> ID: {self.entity_id}")
        print(f"> Heading: {self.headline}")
        print(f"> Review text: {self.text}")
