#test cases

from palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("mom") == True
    assert is_palindrome("dad") == True
    assert is_palindrome("No lemon, no melon") == True
    assert is_palindrome("never odd or even") == True
    assert is_palindrome("2002") == True

def test_is_not_palindrome():
    assert is_palindrome("lights") == False
    assert is_palindrome("city") == False
    assert is_palindrome("mark") == False
    assert is_palindrome("ball") == False

def test_empty_string_is_palindrome():
    assert is_palindrome("") == True

def test_single_character_is_palindrome():
    assert is_palindrome("g") == True
    assert is_palindrome("k") == True
    assert is_palindrome("9") == True

def test_whitespace_is_palindrome():
    assert is_palindrome("  ") == True
    assert is_palindrome("   ") == True
    assert is_palindrome("  s  ") == True
    assert is_palindrome("  2  ") == True

def test_case_insensitive():
    assert is_palindrome("Radar") == True
    assert is_palindrome("No lemon, no melon") == True
    assert is_palindrome("MaDaM") == True
    assert is_palindrome("MoM") == True