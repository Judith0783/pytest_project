from lib.greet import greet

def test_person_of_given_name():
     result = greet("Amparo")
     assert result == "Hello, Amparo!"