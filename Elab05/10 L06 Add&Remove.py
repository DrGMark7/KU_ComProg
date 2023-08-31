Number = list(map(int,input().split()))

def Check_command(T,In):
    if T == "A":
        Number.append(In)
    elif T == "S":
        print(Number[In])
    elif T == "R":
        Number.pop(In)


while True:
    Command,Index = input().split()
    Index = int(Index)
    if Command == 'E' and Index == 0:
        print(*Number)
        break
    else:
        Check_command(Command,Index)