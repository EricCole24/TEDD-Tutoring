import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(hashed_password, user_password):
   password= hashed_password
   return password == hashlib.sha256( user_password.encode()).hexdigest()
