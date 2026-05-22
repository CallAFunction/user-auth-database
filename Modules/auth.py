import bcrypt 

#hashes entered password
def hash(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

#function for verifying entered password
def verify(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)
 