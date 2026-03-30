import bcrypt 

def hash(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
def verify():
    pass
    
    