import key_generator
import os

class User:
    def __init__(self, username, password, passphrase):
        self.username = username
        self.password = password
        self.key = key_generator.pbkdf2(passphrase, os.random(16), 10000, 32)
