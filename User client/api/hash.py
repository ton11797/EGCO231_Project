import hashlib

def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()
    
def check_password(hashed_password, user_password):
    password= hashed_password
    return password == hashlib.sha256(user_password.encode()).hexdigest()
 
new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
