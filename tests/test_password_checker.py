from lib.password_checker import *
import pytest

 #IF the lenght of password is >= 8 return true

def test_check_the_lenght_of_password_if_correct():
    pswd = PasswordChecker()
    result = "password123"
    assert pswd.check(result) == True
     

 #If password is less than 7 characters, raise Exception with message ("Invalid password, must be 8+ characters.")  

def test_for_errors():
    pswd = PasswordChecker()
    result = "hello"
    with pytest.raises(Exception) as e:
        pswd.check(result)
        message = str(e.value)
        assert message == "Invalid password, must be 8+ characters."
        
       
    
