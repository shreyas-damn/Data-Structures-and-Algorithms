#the key is a string
def get_hash(key):
    h=0
    for char in key:
        #ord gets ascii value of character
        h+=ord(char)
    return h

print(get_hash("Bhavadharani"))