class Review:
    def __init__(self, review_id, headline, text, product_id):
        self.review_id = review_id
        self.headline = headline
        self.text = text
        self.product_id = product_id

    def print(self):
        print(f"> Heading: {self.headline}")
        print(f"> Review text: {self.text}")
