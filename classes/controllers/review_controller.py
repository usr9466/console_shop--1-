from classes.controllers.db import DB

'''
   Review Controller 
'''
class ReviewController(DB):
    def __init__(self):
        super(ReviewController, self).__init__()

    def put(self, id, new_entity):
        if(id == None): raise ValueError('id is required')
        if(new_entity == None): raise ValueError('new entity is required')
        if(new_entity.headline == None): raise ValueError('headline is required')
        if(new_entity.text == None): raise ValueError('text is required')
        if(new_entity.product_id == None): raise ValueError('product id is required')
        return super(ReviewController, self).put(id, new_entity)
    
    def post(self, new_entity):
        if(new_entity == None): raise ValueError('new entity is required')
        if(new_entity.headline == None): raise ValueError('headline is required')
        if(new_entity.text == None): raise ValueError('text is required')
        if(new_entity.product_id == None): raise ValueError('product id is required')
        return super(ReviewController, self).post(new_entity)

    def get(self, id):
        if id == None: raise ValueError('id is required')
        return super(ReviewController, self).get(id)
            
    