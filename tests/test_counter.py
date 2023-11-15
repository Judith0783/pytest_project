from lib.counter import Counter

#Initially reports a count of zero.

def test_counter_initially_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."
    
# When we add a single number to the counter
# it is reflected in the final count

def test_counter_adds_a_single_number_to_the_count():
    counter  = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."
    
    
# When we add multiple numbers to the counter
# the sum of those number is the final.

def test_counter_adds_multiple_numbers_to_the_count():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == "Counted to 8 so far."