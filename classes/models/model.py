from uuid import uuid4
'''
    base model class
'''
class Model:
    '''
        init the base model and create a main primary key
    '''
    def __init__(self):
        self.entity_id = uuid4().hex[:4] #id with length = 4