def is_palindrome(s: str) -> bool:
    # Remove spaces and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
