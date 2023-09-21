def count(word, ch, result):

    if len(word) == 1 and word in ch:
        return 1
    elif len(word) == 1:
        return 0
    
    result = count(word[0],ch,result)+count(word[1:],ch,result)
    return result

print(count("aaa", "a", 0))