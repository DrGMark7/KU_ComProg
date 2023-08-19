x = int(input())
y = int(input())
z = int(input())
i = x
p = []
while True:
  if i%z != 0 and i < y:
    p.append(i)
    i += 1
  elif i%z == 0 and i < y:
    i += 11
  elif i%z != 0 and i == y:
    p.append(i)
    break
  else:
    break
for i in range(len(p)):
  if i == 0:
    print(p[i], end = ' ')
  elif (i)%10 != 0:
    print(p[i], end = ' ')
    continue
  else:
    print('')
    print(p[i], end = ' ')
    continue