import pytest #type: ignore
from lib.grammar_stats import *

# If text string is empty, raises an error

def test_check_grammar_empty_string_raises_error():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as err:
        grammar_stats.check("")
    assert str(err.value) == "No text has been inputted to check grammar"

# If sentence starts with a Capital Letter but no puctuation at end, 
# check method returns False
def test_check_grammar_starts_capital_ends_no_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello and welcome")
    assert result == False

# If sentence starts with a Capital Letter and ends with ., 
# check method returns True

def test_check_grammar_starts_capital_ends_full_stop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello and welcome.")
    assert result == True

# If sentence starts with a Capital Letter and ends with !, 
# check method returns True

def test_check_grammar_starts_capital_ends_exclamation_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello and welcome!")
    assert result == True

# If sentence starts with a Capital Letter and ends with ?, 
# check method returns True

def test_check_grammar_starts_capital_ends_question_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello and welcome?")
    assert result == True

# If sentence starts with a Capital Letter and ends with , 
# check method returns False

def test_check_grammar_starts_capital_ends_comma():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello and welcome,")
    assert result == False

# If sentence starts with a Capital Letter and ends with ; 
# check method returns False

def test_check_grammar_starts_capital_ends_semi_colon():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello and welcome;")
    assert result == False

# If sentence doesn't start with a Capital Letter, 
# check method returns False
def test_check_grammar_starts_capital_ends_semi_colon():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello and welcome!")
    assert result == False

# If no texts have been checked, raise error: No texts have been checked
def test_percentage_good_no_texts_checked():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as err:
        grammar_stats.percentage_good()
    assert str(err.value) == "No texts have been checked"

# If one text has been checked and passes return 100

def test_percentage_good_one_text_checked_and_passed():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello!")
    assert grammar_stats.percentage_good() == 100

# If four texts have been checked and 2 pass, return 50

def test_percentage_good_two_texts_checked_and_one_passed():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello!")
    grammar_stats.check("hello")
    assert grammar_stats.percentage_good() == 50

# If three texts have been checked and 2 pass, return 67 (rounds up from 66.6).

def test_percentage_good_three_texts_checked_and_two_passed():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello!")
    grammar_stats.check("hello")
    grammar_stats.check("Hello.")
    assert grammar_stats.percentage_good() == 67


# If three texts have been checked and 1 pass, return 33 (rounds down from 33.3).

def test_percentage_good_three_texts_checked_and_two_passed():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello!")
    grammar_stats.check("hello")
    grammar_stats.check("Hello")
    assert grammar_stats.percentage_good() == 33