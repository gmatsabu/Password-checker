from  password_checker.password_checker import Password
import pytest

Password = "TeBo55Hj"

def test_Password_Exixt():
    assert 1 < len(Password) <=15,"Password must have atleast one input"

def test_Password_lengt():
    assert 8 <= len(Password) <=15, "String must be between 8 and 15 character"
