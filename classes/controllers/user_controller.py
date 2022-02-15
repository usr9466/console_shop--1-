from classes.controllers.db import DB

'''
    User Controller
'''
class UserController(DB):
    def __init__(self):
        super(UserController, self).__init__()

    def put(self, id, new_entity):
        if(id == None): raise ValueError('id is required')
        if(new_entity == None): raise ValueError('new entity is required')
        if(new_entity.firstname == None): raise ValueError('firstname id is required')
        if(new_entity.lastname == None): raise ValueError('lastname id is required')
        if(new_entity.username == None): raise ValueError('username id is required')
        if(new_entity.birthday == None): raise ValueError('birthday id is required')
        if(new_entity.role == None): raise ValueError('role id is required')
        return super(UserController, self).put(id, new_entity)
    
    def post(self, new_entity):
        if(new_entity == None): raise ValueError('new entity is required')
        if(new_entity.firstname == None): raise ValueError('firstname id is required')
        if(new_entity.lastname == None): raise ValueError('lastname id is required')
        if(new_entity.username == None): raise ValueError('username id is required')
        if(new_entity.birthday == None): raise ValueError('birthday id is required')
        if(new_entity.role == None): raise ValueError('role id is required')
        return super(UserController, self).post(new_entity)

    def get(self, id):
        if id == None: raise ValueError('id is required')
        return super(UserController, self).get(id)

    def login(self, username, pw):
        if username == None: raise ValueError('username is required')
        if pw == None: raise ValueError('password is required')
        found_user = next(x for x in self._context.values() if x.username == username and x.password == pw)
        if found_user == None: return False
        return found_user


    
            
    