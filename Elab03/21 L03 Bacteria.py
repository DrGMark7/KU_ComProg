def nb_year(a,b,c,d):
  sum = 0
  i = 0
  while True:
    sum = a + (a * (b/100)) + c
    a = int(sum)
    i += 1
    if sum >= d:
      return i
      break