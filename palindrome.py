def is_palindrome(text):
    text = text.lower()
    text = "".join(char for char in text if char.isalnum())

    return text == text[::-1]