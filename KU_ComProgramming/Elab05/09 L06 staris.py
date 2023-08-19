def draw(m):
  for i in range(1,len(m) + 1):
    print(str(m[i-1])*i)
while True:
  x = str(input())
  if x == '0':
    break
  y = x.split()
  draw(y)
print('Good Bye.')