x = str(input("Input: ")).split()
def commaCode(List):
    text = ""
    if len(List) == 1:
        return List[0]
    elif len(List) == 0:
        return ''
    else:
        text += ", ".join(List[:-1])
        text += ", and "+List[-1]
    return text
print(commaCode(x))