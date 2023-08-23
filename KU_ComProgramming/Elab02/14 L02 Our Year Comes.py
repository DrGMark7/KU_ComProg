M = input("What's the result of Manchester city's match? ")
L = input("What's the result of Liverpool's match? ")
a = ""
if M == L:
    m = input("What is the margin that Manchester city won by? ")
    l = input("What is the margin that Liverpool won by? ")
    if m == l:
        a = input("Which team won the play-off match?(Manchester city/Liverpool) ")
    elif m > l:
        a = "Manchester city"
    elif m < l:
        a = "Liverpool"
elif M == "won":
    a = "Manchester city"
elif L == "won":
    a = "Liverpool"
print(a+" is the champion of Premier League.")