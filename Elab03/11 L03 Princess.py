def caltime(s):
    h = s//3600
    m = (s - (h*3600))//60
    s = s - (h*3600) - (m*60)
    l = (h,m,s)
    return l
s = int(input("s: "))
print(f"{s} seconds equals {caltime(s)[0]} hour(s) {caltime(s)[1]} minute(s) and {caltime(s)[2]} second(s)")

