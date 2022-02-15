
'''
    base db controller for a given dictionary
'''
class DB:
    '''
        init db with an empty dictionary
    '''
    def __init__(self):
        self._context = {}

    '''
        get a specific id element 
        we assume each class provides an attribute named: 'entity_id'
    '''
    def get(self,id):
        try:
            # next gives the first occurance of this ................ condition
            return self._context[id]
        except:
            print('error in db getter')


    '''
        update a specific id element
    '''
    def put(self, id, new_entity):
        try:
            if not id in self._context: raise ValueError('id not found')
            self._context[id] = new_entity
            return True
        except:
            print('error in db putter')
            return False

    '''
        create a specific element
    '''
    def post(self, new_entity):
        try:
            #entity id is a must have, raise error if not given
            if(new_entity.entity_id == None): raise ValueError('no entity id given')
            if new_entity.entity_id in self._context: raise ValueError('id is taken')
            self._context[new_entity.entity_id]= new_entity
            return True
        except:
            print('error in db post')
            return False

    '''
        get whole list
    '''
    def get_all(self):
        try:   
            return self._context.values()
        except:
            print('error in getAll')
            return False

    '''
        get Dictionary
    '''
    def get_dict(self):
        return self._context