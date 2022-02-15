from classes.controllers.db import DB

'''
   Product Controller 
'''
class ProductController(DB):
    '''
        no special init
    '''
    def __init__(self):
        super(ProductController, self).__init__()

    '''
        update entity and check if it is valid
    '''
    def put(self, id, new_entity):
        if(id == None): raise ValueError('id is required')
        if(new_entity == None): raise ValueError('new entity is required')
        if(new_entity.name == None): raise ValueError('name id is required')
        if(new_entity.description == None): raise ValueError('description id is required')
        if(new_entity.price_netto == None): raise ValueError('price_netto id is required')
        if(new_entity.price_brutto == None): raise ValueError('price_brutto id is required')
        if(new_entity.in_stock == None): raise ValueError('in_stock id is required')
        if(new_entity.category == None): raise ValueError('category id is required')
        return super(ProductController, self).put(id, new_entity)
    
    '''
        create entity and check if it is valid
    '''
    def post(self, new_entity):
        if(new_entity == None): raise ValueError('new entity is required')
        if(new_entity.name == None): raise ValueError('name id is required')
        if(new_entity.description == None): raise ValueError('description id is required')
        if(new_entity.price_netto == None): raise ValueError('price_netto id is required')
        if(new_entity.price_brutto == None): raise ValueError('price_brutto id is required')
        if(new_entity.in_stock == None): raise ValueError('in_stock id is required')
        if(new_entity.category == None): raise ValueError('category id is required')
        return super(ProductController, self).post(new_entity)

    '''
        gets entity if an id is given
    '''
    def get(self, id):
        if id == None: raise ValueError('id is required')
        return super(ProductController, self).get(id)
            
