command = str(input("Direction to flip square (V/H): "))
size = int(input("Input size of square: "))
twoD_List = []
for _ in range(size):
    twoD_List.append(list(map(str,input().split())))

def reflip(array,cmd):
    tempm = array.copy()
    if cmd=='H':
        for i in range(0,len(tempm),1):
                tempm[i].reverse()
    elif cmd=='V':
        tempm.reverse()
    return(tempm)

print("After flip:")
for i in reflip(twoD_List,command):
    print(' '.join(i))