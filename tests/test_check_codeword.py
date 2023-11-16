from lib.check_codeword import check_codeword

"""
If the codeword is correct
Returns "Correct! Come in." 
"""

def test_with_correct_codeword():
     result = check_codeword("horse")
     assert result == "Correct! Come in."
     
"""
If the codeword if wrong 
Return "WRONG!"
"""
         
def test_with_incorrect_codeword():
    result = check_codeword("water")
    assert result == "WRONG!"
    
"""
If the codeword has the rigth first and last letter
Returns "close, but nope."
"""

def test_with_close_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."
    
"""
If the codeword has the right first letter and the wrong last one 
Returns "WRONG!"
"""
def test_with_right_first_letter_and_wrong_last_letter():
    result = check_codeword("hat")
    assert result == "WRONG!"   
    
"""
If the codeword has the wrong first letter and the right last one
Returns "WRONG!"
"""
def test_with_wrong_first_letter_and_rigth_last_letter():
    result = check_codeword("mouse")
    assert result == "WRONG!"   
 

