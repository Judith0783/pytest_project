from lib.gratitudes import * 

"""
Create a gratitude
"""
def test_create_a_gratitude():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []


"""
Adding a gratitude
to an array
"""
def test_adding_a_gratitude():
    added_gratitude = Gratitudes()
    added_gratitude.add("Thankful")
    assert added_gratitude.gratitudes == ["Thankful"]


"""
Format gratitudes
Concatenation
"""
def format_gratitude():
    formatted_gratitude = Gratitudes() 
    formatted_gratitude.add("Patience")
    formatted_gratitude.add("Happiness")
    assert formatted_gratitude.format() == "Be grateful for: Patience, Happiness"