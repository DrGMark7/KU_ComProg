t = int(input("How long have Buzz played ?: "))
h = t//60
m = t - h*60
c = 0
if m > 20:
    h = h+1
if h in range(2,4):
    c = (h*900)*0.9
elif h in range(1,3):
    c = (h*900)
elif h == 4:
    c = (h*900)*0.8
elif h > 4:
    c = (h*900)*0.7
print(f"Total price is {round(c)} baht.")