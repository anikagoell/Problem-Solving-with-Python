def is_palindrome(value):
    """
    Check whether the given input (string or integer) is a palindrome.

    Arguments:
        value (str or int): Input value

    Returns:
        bool: True if palindrome, else False
    """

    # Convert everything to string for simplicity
    s = str(value).lower()
    #Declaring two pointers, one at the start and one at the end of the string
    left, right = 0, len(s) - 1
    # Move the pointers towards the center, comparing characters
    while left < right:
        if s[left] != s[right]:
            return False # If characters don't match, it's not a palindrome
        left += 1
        right -= 1

    return True # If we successfully compared all characters, it's a palindrome


if __name__ == "__main__":  
    user_input = input("Enter a string or integer: ")

    # Try converting to int if possible
    try:
        user_input = int(user_input)
    except ValueError:
        pass

    print(is_palindrome(user_input))
    