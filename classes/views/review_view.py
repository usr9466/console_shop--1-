from classes.models.Review import Review
from classes.views.view import View

'''
    the review interface
'''
class ReviewView(View):
    '''
        init the view
    '''
    def __init__(self):
        super(ReviewView, self).__init__('review')
    
    '''
        create a reviwe and returns
    '''
    def write_review(self, product_ids):

        valid = False
        while(not valid):
            print("> Für welches Produkt wollen Sie einen Bericht schreiben?")
            prod_id = self.custom_input()
            valid = prod_id in product_ids
            if not valid:
                print("Keine valide Eingabe, bitte erneut eingeben...")
                for key in product_ids:
                    print(key)

        print("> Bitte geben Sie die Überschrift ihrer Bewertung ein")
        heading = self.validate_input_loop("review_heading")

        print("> Bitte geben Sie den Inhalt ihres Berichtes ein")
        review_text = self.validate_input_loop("review_text")


        review = Review(heading,review_text,prod_id)
        
        return review


    def view_reviews(self,product_id2product, reviews):
        valid = False
        
        while not valid:
            print("> Für welche Produkte wollen Sie die Berichte sehen?")
            prod_id = self.custom_input()
            valid = prod_id in product_id2product
            if not valid:
                print("Keine valide Eingabe, bitte erneut eingeben...")
                for key in product_id2product:
                    print(key)

        print(f"> Alle Berichte zu der Prdukt-ID: {prod_id}")
        i = 1
        for review in reviews:
            if review.product_id == prod_id:
                print(f"> Review {i}:")
                review.print()
                print("")
                i += 1
