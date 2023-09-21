def reverse_string(word):
    Word = list(word)
    if len(word) == 1 and word in Word:
        return Word[0]
    
    return reverse_string(word[1:])+ reverse_string(word[0]) 

print(reverse_string('hello'))