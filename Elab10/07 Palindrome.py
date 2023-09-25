def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
    
print(is_palindrome('redder'))