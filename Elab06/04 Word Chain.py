Text = str(input('Text: ')).split()
size = len(Text[0])
ins_index = []

for i in range(len(Text)):
    try:
        A,B = Text[i],Text[i+1]
    except:
        pass
    
    index = []
    for a,b in zip(range(len(A)),range(len(B))):
        if A[a] == B[b]:
            index.append(a)

    ins_index.append(index)

count_chain = []
count_length = 1
for i in ins_index[:-1]:
    if len(i) > size-3:
        count_length += 1
    else:
        count_chain.append(count_length)
        count_length = 1

count_chain.append(count_length)

print(f'{len(count_chain)} Chain(s). Maximum length is {max(count_chain)} word(s).')