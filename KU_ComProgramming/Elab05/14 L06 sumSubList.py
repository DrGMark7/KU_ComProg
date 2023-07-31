number = list(map(int,input().split()))
while True:
    x,y = input().split()
    x,y = int(x),int(y)
    if not(-1*len(number) <= x <= len(number)-1) and not(-1*len(number) <= y <= len(number)-1):
        print("x and y Bad Input")
    elif not(-1*len(number) <= x <= len(number)-1):
        print("x Bad Input")
    elif not(-1*len(number) <= y <= len(number)-1):
        print("y Bad Input")
    else:
        x,y = x%len(number),y%len(number)
        if (x >=  0) and (y >= 0):
            if x > y:
                break
            else:   
                print(sum(number[x:y+1]))
        
    
