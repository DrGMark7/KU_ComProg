Text = str(input("Text: "))
sub = list(str(input("Substring: ")))

index = []
TextList = list(Text)

for i in range(len(TextList)):
    item = TextList[i:i+len(sub)]
    print(item)
    if item == sub:
        del TextList[i:i+len(sub)]
        TextList.insert(i,f'[{"".join(sub)}]')
        index.append(i)

print(''.join(TextList))