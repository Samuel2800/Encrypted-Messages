import hashlib
import hmac

def pbkdf2(password, salt, iterations, key_length):
    derived_key = b""

    #this loop is for the number of times the hash function is applied 
    #in order to make the computation expensive and for it to be secure
    for i in range(iterations):
        data = password + salt + i.to_bytes(4, byteorder='big')
        #creates a Hash-based Message Autenticated Code involving a 
        #cryptographic hash function combinated with a secret key
        #the sha-256 is a cryptographic hash function that takes an input message 
        #and returns a 256-bit hash value
        block = hmac.new(password, data, hashlib.sha256).digest()
        #here I used a XOR operator between the previous derived_key and the current block
        derivated_key = bytes(x ^ y for x, y in zip(derived_key, block))

    return derivated_key[:key_length]