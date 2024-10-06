def is_anagram(str1, str2):
    # Normalize the strings by converting to lowercase and removing spaces
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if lengths are the same
    if len(str1) != len(str2):
        return False

    # Sort both strings and compare
    return sorted(str1) == sorted(str2)


print(is_anagram("Listen", "Silent")) 
print(is_anagram("Hello", "Olelh"))   
print(is_anagram("Test", "Taste"))   