Finish = int(input("Distance from starting point(m.): "))
action_forward , action_backward ,all_action= [],[],[]
x = 0
count = 0
def forward(x):
    x = x+5
    action_forward.append(x)
    all_action.append(x)
    x = x-2
    action_forward.append(x)
    all_action.append(x)
    return x

def backward(x):
    x = x-4
    action_backward.append(x)
    all_action.append(x)
    x = x+3
    action_backward.append(x)
    all_action.append(x)
    return x

if Finish == 0:
    all_action.append(0)

while Finish != x:
    if x < Finish:
        x = forward(x)
        count += 1
    elif x > Finish:
        x = backward(x)
        count += 1
print(' '.join(map(str,all_action)))
print(f"Buzz moved {count} set(s)")
    
