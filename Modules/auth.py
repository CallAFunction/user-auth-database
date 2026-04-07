'''import bcrypt 

def hash(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def verify(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)


 '''   