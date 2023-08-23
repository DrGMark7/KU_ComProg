import statistics as s
x = []
for i in ['a','b','c','d','e']:
    x.append(float(input(f"Input {i}: ")))
print(f'mean: {s.mean(x):.3f}')
m,a= round(s.mean(x),3),0
for i in x:
    a = a+(i-m)**2
print(f'sd: {(a/len(x))**0.5:.3f}')  