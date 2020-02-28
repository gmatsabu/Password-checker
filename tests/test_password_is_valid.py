from password_checker.password_checker import Password
import pytest

Password = "TeBo55Hj"
special_char = "$#@!*"
#print(any(c.isupper() for c in Password)) #true

# passs ="matdsA122$p"
# checker = Password(passs)

# def test_password_is_valid():
#     assert checker.lowercase() == True
#password = Password()

def test_Password_lengt():
    assert 8 <= len(Password) <=15, "String must be between 8 and 15 character"

def test_lowercase():
    assert any(c.islower() for c in Password)," String must Contain atleast  one lower case"

def test_uppercase():
    assert any(c.isupper() for c in Password),"String must Contain atleast one upper case " 

def test_digit():
    assert any(c.isdigit() for c in Password),"String must Contain atleast one digit"

def test_special():
    assert any(special_char for c in Password),"String must Contain atleast one specialCase"





    

# while True:
#     validate = input()
#     try:
#         assert 8 <= len(validate) <= 15, "String must be between 8 and 15 character"

#         break # if we have on errors then the password can pass
#     except Exception as e:
#         print(e)
