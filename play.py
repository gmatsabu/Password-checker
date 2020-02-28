
from getpass import getpass
import string

def check_contains(input, letters):
    return any(char in letters for char in input)

def validate_password(input):
    valid = True
    if not check_contains(input, string.ascii_uppercase):
        valid = False
        print ("Password needs at least one upper-case character")
    if not check_contains(input, string.ascii_lowercase):
        valid = False
        print ("Password needs at least one lower-case character.")
    if not check_contains(input, string.digits):
        valid = False
        print ("Password needs at least one number.")
    if not check_contains(input, string.punctuation + '#'):
        valid = False
        print ("Password needs at least one special character.")
    if len(input) < 8:
        valid = False
        print ("Password needs to be at least 8 characters in length.")
    return valid

while True:
    password = getpass("Enter desired password: ")
    if validate_password(password):
        print ("Valid password")
        break