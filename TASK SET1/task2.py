def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
