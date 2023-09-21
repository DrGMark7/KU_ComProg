def count_vowel(word):
    vowel = ['a','e','i','o','u']

    if len(word) == 1 and word.lower() in vowel:
        return 1
    elif len(word) == 1:
        return 0
    
    return count_vowel(word[0])+count_vowel(word[1:])

print(count_vowel('Hello'))