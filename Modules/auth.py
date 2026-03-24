import bcrypt 

def hash(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt)
    